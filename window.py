#!/usr/bin/env python
import sys
import widgets
import time
while True:
    sys.stdout.write(widgets.get_widow_name())
    sys.stdout.flush()
    time.sleep(0.5)
