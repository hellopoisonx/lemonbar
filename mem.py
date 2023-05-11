#!/usr/bin/env python
# import os
import sys
import time
import widgets
while True:
    sys.stdout.write(widgets.get_memory())
    sys.stdout.flush()
    time.sleep(3)
