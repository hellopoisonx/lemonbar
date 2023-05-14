#!/usr/bin/env python
import sys
import widgets
import time
import action
click_event = action.Right[-3].click_event
click_cmd = action.Right[-3].click_cmd
click_start = ""
click_end= ""
for i, event in enumerate(click_event):
    click_start += "%{A" + str(event) + ":" + click_cmd[i] + " :}"
    click_end += " %{A}"
while True:
    sys.stdout.write(click_start + widgets.get_light() + click_end)
    sys.stdout.flush()
    time.sleep(0.5)
