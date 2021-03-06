"""
Implementation of Nazgul application

Which periodically collects information about what processes are executed in
the OS, and takes a screenshots, and then sends them to the server of the
Sauron system.
"""

import collections
import datetime
import json
import logging
import logging.config
import os
import os.path
import platform

import mss
import psutil
import requests
import requests.auth


logging.config.fileConfig('logging.conf')


def _get_current_user():
    return psutil.users()[0].name


def _get_current_processes():
    """
    Gets list of processes currently executed in the OS

    List of processes is a list of dicts, where every dict represents
    single process. Retrieved information about a process are:
    - PID,
    - name,
    - command line arguments,
    - username which started the process,
    - time of creation.
    """
    return [p.as_dict(attrs=['pid',
                             'name',
                             'cmdline',
                             'username',
                             'create_time']) for p in psutil.process_iter()]


def _update_alarms(blacklisted_processes, processes):
    any_alarm_occurred = False
    for p in processes:
        p.update({'alarm': p['name'] in blacklisted_processes})
        any_alarm_occurred |= p['alarm']
    return any_alarm_occurred


class Timer:
    """Class implementing functionality of the simple timer"""

    def __init__(self, timedelta):
        self.start = datetime.datetime.utcnow()
        self.timedelta = timedelta

    def countdown_over(self):
        """Checks if countdown of the timer is over"""
        return datetime.datetime.utcnow() - self.start >= self.timedelta

    def restart(self):
        """Restarts the timer"""
        self.start = datetime.datetime.utcnow()


class Nazgul:
    """Class implementing the highest level of abstraction of the module functionality"""

    def __init__(self, config):
        self.config = config
        self.current_user = _get_current_user()
        try:
            self.name = self.config['name']
        except KeyError:
            self.name = self.current_user
            logging.warning(
                "no 'name' property in the config; assigned current user name (%s)",
                self.name)
        self.timers = {
            'processes collecting': Timer(datetime.timedelta(seconds=5)),
            'server communication': Timer(datetime.timedelta(
                seconds=config['time period']['server communication'])),
            'screenshot': Timer(datetime.timedelta(seconds=30))}
        self.processes = []
        self.blacklist = {'processes': []}
        self.screenshooter = mss.mss()
        self.screenshots_directory = os.path.join(os.path.curdir, 'screenshots')
        os.makedirs(self.screenshots_directory, exist_ok=True)
        self.screenshots_to_send = []
        self.auth = requests.auth.HTTPBasicAuth(self.name, self.config['password'])

    def _filter_processes(self, processes):
        if platform.system() == 'Windows':
            processes_username = '{}\\{}'.format(platform.node(), self.current_user)
        else:
            processes_username = self.current_user
        return [p for p in processes if p['username'] == processes_username]

    def _shoot_screenshot(self):
        current_datetime = datetime.datetime.utcnow()
        filename = '{}-{}-{:%Y%m%d%H%M%S}.png'.format(self.name, self.config['group'], current_datetime)
        filepath = os.path.join(self.screenshots_directory, filename)
        self.screenshooter.shot(mon=-1, output=filepath)
        return collections.namedtuple('ScreenshotFile', 'filepath, create_time')._make([filepath, int(current_datetime.timestamp())])

    def run(self):
        """Runs Nazgul application"""
        logging.info('getting blacklist from server for the first time')
        if not self._update_blacklist():
            logging.error('getting blacklist unsuccessfully')
        while True:
            if self.timers['processes collecting'].countdown_over():
                self.timers['processes collecting'].restart()
                processes = self._filter_processes(_get_current_processes())
                any_alarm_occured = _update_alarms(self.blacklist['processes'], processes)
                if any_alarm_occured:
                    logging.info('alarm occured')
                collected_processes = {'nazgul': self.name,
                                       'group': self.config['group'],
                                       'processes': processes,
                                       'create_time': int(datetime.datetime.utcnow().timestamp()),
                                       'alarm': any_alarm_occured}
                self.processes.append(collected_processes)
                logging.info('%s processes collected at %s (utc)',
                             len(collected_processes['processes']),
                             collected_processes['create_time'])
            if self.timers['screenshot'].countdown_over():
                self.timers['screenshot'].restart()
                logging.info('shooting screenshot')
                self.screenshots_to_send.append(self._shoot_screenshot())
            if self.timers['server communication'].countdown_over():
                self.timers['server communication'].restart()
                logging.info('updating blacklist from server')
                if not self._update_blacklist():
                    logging.error('updating blacklist unsuccessfully')
                logging.info('sending collection of processes to server')
                if self._send_processes_to_server(self.processes):
                    self.processes.clear()
                else:
                    logging.error('collection of processes sent to server unsuccessfully')
                logging.info('sending %s screenshots to server', len(self.screenshots_to_send))
                self.screenshots_to_send = [s for s in self.screenshots_to_send
                                            if not self._send_screenshot(s)]
                if self.screenshots_to_send:
                    logging.error('%s screenshots sent to server unsuccessfully',
                                  len(self.screenshots_to_send))
                for screenshot_filepath in [os.path.join(self.screenshots_directory, s) for s in os.listdir(self.screenshots_directory)]:
                    if screenshot_filepath not in [s.filepath for s in self.screenshots_to_send]:
                        os.remove(screenshot_filepath)
                        logging.info('%s removed', screenshot_filepath)

    def _send_processes_to_server(self, processes):
        url = '{0[hostname]}{0[process_endpoint]}'.format(self.config['server'])
        logging.debug('sending to: %s', url)
        try:
            response = requests.post(url, json=processes, auth=self.auth)
        except requests.exceptions.ConnectionError as e:
            logging.error(e)
            return False
        if not response.ok:
            logging.error('response: %s %s', response.status_code, response.reason)
        return response.ok

    def _send_screenshot(self, screenshot):
        with open(screenshot.filepath, 'rb') as file:
            url = '{0[hostname]}{0[screenshots_endpoint]}'.format(self.config['server'])
            logging.debug('sending to: %s', url)
            params = {
                'create_time': screenshot.create_time,
                'group': self.config['group']}
            try:
                response = requests.post(url, files={'screenshot': file.read()}, params=params, auth=self.auth)
            except requests.exceptions.ConnectionError as e:
                logging.error(e)
                return False
            if not response.ok:
                logging.error('response: %s %s', response.status_code, response.reason)
            return response.ok

    def _update_blacklist(self):
        url = '{0[hostname]}{0[blacklist_endpoint]}'.format(self.config['server'])
        logging.debug('getting from: %s', url)
        params = {
            'group': self.config['group']}
        try:
            response = requests.get(url, params=params, auth=self.auth)
        except requests.exceptions.ConnectionError as e:
            logging.error(e)
            return False
        if response.ok:
            response_json = json.loads(response.content.decode())
            if response_json:
                self.blacklist = response_json[0]
                logging.debug('current blacklist: %s', self.blacklist)
            else:
                logging.warning('got empty blacklist json')
        else:
            logging.error('response: %s %s', response.status_code, response.reason)
        return response.ok



def main():
    """Main function"""
    with open('config.json', 'r') as file:
        config = json.load(file)
    logging.info('creating Nazgul from the config: %s', config)
    Nazgul(config).run()


if __name__ == "__main__":
    logging.info('application started')
    try:
        main()
    except KeyboardInterrupt:
        logging.info('application stopped')
    except:
        logging.exception('unhandled exception')
        raise
