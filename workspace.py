#!/usr/bin/env python
import sys
import widgets
while True:
    sys.stdout.write(widgets.get_current_workspace())
    sys.stdout.flush()
