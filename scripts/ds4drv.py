# python script for managing ds4drv in daemon mode

import os
from pathlib import Path
import subprocess

# path to the ds4drv daemons pid file
filepath = "/tmp/ds4drv.pid"

# check if the pid file exists
if os.path.exists(filepath): # if True, then daemon is running

    pid = None # get the pid of the daemon process
    with open(filepath) as file:
        pid = file.read()

    subprocess.run(["kill",pid]) # kill the process
    result = subprocess.run(["notify-send","'ds4drv daemon at {} killed'".format(pid)]) # send notification

else: # if False, daemon is not running

    # run daemon
    subprocess.run(["ds4drv","--daemon"])

    # output
    with open(filepath) as file: 
        subprocess.run(["notify-send","'ds4drv daemon started at {}'".format(file.read())])
