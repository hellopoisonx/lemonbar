#!/usr/bin/env python
# import os
import time
import sys
import widgets
import action
click_event = action.Right[1].click_event
click_cmd = action.Right[1].click_cmd
click_start = ""
click_end= ""
for i, event in enumerate(click_event):
    click_start += "%{A" + str(event) + ":" + click_cmd[i] + " :}"
    click_end += " %{A}"
while True:
    sys.stdout.write(click_start + widgets.clock() + click_end)
    sys.stdout.flush()
    time.sleep(10)

