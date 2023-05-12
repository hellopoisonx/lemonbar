#!/usr/bin/env python
import os
import action
import time
lemonbar = "lemonbar -p -o 1 "
os.popen("killall lemonbar")
x = 1750
for i, widget in enumerate(action.Right):
    position = str(widget.width) + "x" + "27" + "+" + str(x) + "+" + "1" 
    cmd = widget.cmd + ' | ' + lemonbar + "-f " + widget.font + " -F " + '"' + widget.forecolor + '"' + " -B " + '"' + widget.backcolor + '"' + " -g " + position + " &"
    x = x + widget.width + widget.gap
    print(str(x) + " " + cmd)
    os.popen(cmd)
x = 10
for i, widget in enumerate(action.Left):
    position = str(widget.width) + "x" + "25" + "+" + str(x) + "+" + "1" 
    cmd = widget.cmd + ' | ' + lemonbar + "-f " + widget.font + " -F " + '"' + widget.forecolor + '"' + " -B " + '"' + widget.backcolor + '"' + " -g " + position + " &"
    x = x + widget.width + widget.gap
    print(str(x) + " " + cmd)
    os.popen(cmd)
