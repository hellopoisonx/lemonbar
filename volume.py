#!/usr/bin/env python
# import os
import sys
import widgets
import time
while True:
    sys.stdout.write(widgets.get_volume())
    sys.stdout.flush()
    time.sleep(1)
