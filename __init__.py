#!/usr/bin/env python
import os
import action
# widgets = ["show_all_workspace", "clock_hour", "clock_year", "cpu", "net", "volume", "mem"]
lemonbar = "lemonbar -p  -f 'Font Awesome 6 Free' "
os.popen("killall lemonbar")
x = 20
for i, widget in enumerate(action.Left):
    position = str(widget.width) + "x" + "27" + "+" + str(x) + "+" + "1" 
    cmd = widget.cmd + ' | ' + lemonbar + "-f " + widget.font + " -F " + '"' + widget.forecolor + '"' + " -B " + '"' + widget.backcolor + '"' + " -g " + position + " &"
    x = x + widget.width + widget.gap
    print(str(x) + " " + cmd)
    os.popen(cmd)
x = 1700
for i, widget in enumerate(action.Right):
    position = str(widget.width) + "x" + "27" + "+" + str(x) + "+" + "1" 
    cmd = widget.cmd + ' | ' + lemonbar + "-f " + widget.font + " -F " + '"' + widget.forecolor + '"' + " -B " + '"' + widget.backcolor + '"' + " -g " + position + " &"
    x = x + widget.width + widget.gap
    print(str(x) + " " + cmd)
    os.popen(cmd)
