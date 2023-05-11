#!/usr/bin/env python
# import os
import sys
import widgets
import time
while True:
    sys.stdout.write(widgets.get_net_rate())
    sys.stdout.flush()
    time.sleep(1)
