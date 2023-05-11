#!/usr/bin/env python
# import os
import time
import sys
import widgets
while True:
    sys.stdout.write(widgets.get_cpu())
    sys.stdout.flush()
    time.sleep(2)
