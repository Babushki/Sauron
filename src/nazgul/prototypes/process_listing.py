import datetime
import json

import psutil

NAZGUL_NAME = [u.name for u in psutil.users() if u.host == 'localhost'][0]
PROCESSES = [p.as_dict(attrs=['pid',
                              'name',
                              'cmdline',
                              'username',
                              'create_time']) for p in psutil.process_iter()]
OUTPUT = {'nazgul': NAZGUL_NAME,
          'processes': PROCESSES,
          'create_time': datetime.datetime.now().utcnow().timestamp()}
print(json.dumps(OUTPUT, indent=4))
