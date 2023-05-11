#!/usr/bin/env python
import sys
import widgets
import time
while True:
    sys.stdout.write(widgets.get_current_workspace())
    time.sleep(1)
    sys.stdout.flush()
