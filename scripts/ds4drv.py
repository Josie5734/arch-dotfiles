# python script for managing ds4drv in daemon mode

import os
from pathlib import Path
import subprocess
import time

# path to the ds4drv daemons pid file
pidfilepath = "/tmp/ds4drv.pid"

# path to the ds4drv daemons log file
logfilepath = "~/.cache/ds4drv.log"

# check if the pid file exists
if os.path.exists(pidfilepath): # if True, then daemon is running

    pid = None # get the pid of the daemon process
    with open(pidfilepath) as file:
        pid = file.read()

    subprocess.run(["kill",pid]) # kill the process
    subprocess.run(["notify-send","'ds4drv daemon at {} killed'".format(pid)]) # send notification

else: # if False, daemon is not running

    # run daemon
    subprocess.run(["ds4drv","--daemon"])

    # output
    with open(pidfilepath) as file: 
        subprocess.run(["notify-send","'ds4drv daemon started at {}'".format(file.read())])
