#!/usr/bin/env python
import sys
import widgets
import time
# import time
while True:
    sys.stdout.write(widgets.get_current_workspace())
    time.sleep(0.2)
    sys.stdout.flush()
