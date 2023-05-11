#!/usr/bin/env python
# import os
import time
import sys
import widgets
while True:
    sys.stdout.write(widgets.clock_hour())
    sys.stdout.flush()
    time.sleep(30)

