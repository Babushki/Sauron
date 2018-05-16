"""
Implementation of Nazgul application

Which periodically collects information about what processes are
executed in the OS, and what websites are visited by currently logged
user, and then sends them to the server of the Sauron system.
"""

import datetime
import json
import logging
import logging.config

import psutil


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
        try:
            self.name = self.config['name']
        except KeyError:
            self.name = _get_current_user()
            logging.warn(
                "no 'name' property in the config; assigned current user name (%s)",
                self.name)
        self.processes_collecting_timer = Timer(datetime.timedelta(
            seconds=config['time period']['processes collecting']))
        self.server_communication_timer = Timer(datetime.timedelta(
            seconds=config['time period']['server communication']))
        self.processes = []

    def run(self):
        """Runs Nazgul application"""
        while True:
            if self.processes_collecting_timer.countdown_over():
                self.processes_collecting_timer.restart()
                collected_processes = {'processes': _get_current_processes(),
                                       'create_time': datetime.datetime.now().utcnow().timestamp()}
                self.processes.append(collected_processes)
                logging.info('%s processes collected at %s (utc)',
                             len(collected_processes['processes']),
                             collected_processes['create_time'])
            if self.server_communication_timer.countdown_over():
                self.server_communication_timer.restart()
                if self._send_processes_to_server():
                    logging.info('%s process collections sent to server', len(self.processes))
                    self.processes.clear()
                else:
                    logging.error('sending process collections to server unsuccessful')

    def _send_processes_to_server(self):
        identified_processess = self.processes
        for p in identified_processess:
            p.update({'name': self.name, 'group': self.config['group']})
        # Temporary "mockup" {
        with open('nazgul-{:%Y%m%d%H%M%S}.json'.format(datetime.datetime.now()), 'w') as file:
            json.dump(identified_processess, file, sort_keys=True, indent=4)
        # }
        return True


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
