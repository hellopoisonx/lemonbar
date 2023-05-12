#!/usr/bin/env python
import os
import action
import time
lemonbar = "lemonbar -p -o 1 -u 3 "
os.popen("killall lemonbar")
def drawbar(x, layout):
    for _, widget in enumerate(layout):
        position = str(widget.width) + "x" + "27" + "+" + str(x) + "+" + "1" 
        cmd = widget.cmd + ' | ' + lemonbar + "-f " + widget.font + " -F " + '"' + widget.forecolor + '"' + " -B " + '"' + widget.backcolor + '"' + " -g " + position + " &"
        x = x + widget.width + widget.gap
        print(str(x) + " " + cmd)
        os.popen(cmd)
#draw right bar
drawbar(1760, action.Right)
#draw middle bar
drawbar(1000, action.Middle)
#draw left bar
drawbar(10, action.Left)
