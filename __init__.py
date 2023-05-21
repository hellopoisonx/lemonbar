#!/usr/bin/env python
import os
import action
import log

lemonbar = "lemonbar -p -o 1 -u 3 "


def handle_mouse_event(obj: action.action):
    if obj.click_event is None:
        return ("", "")
    event_start = ""
    event_end = ""
    for i, item in enumerate(obj.click_event):
        event_start += "%{A" + str(item) + ":" + obj.click_cmd[i] + ":}"
        event_end = "%{A" + str(item) + "}" + event_end
    return (event_start, event_end)


def drawbar(x, layout):
    for _, widget in enumerate(layout):
        event = handle_mouse_event(widget)
        position = str(widget.width) + "x" + "27" + "+" + str(x) + "+" + "1"
        shell_cmd = "(while true\n do\n echo \"" + \
            event[0] + "$(" + widget.cmd + ")" + event[1] + \
            "\";sleep " + str(widget.interval) + "s;\ndone)"
        cmd = shell_cmd + ' | ' + lemonbar + "-f " + widget.font + " -F " + '"' + widget.forecolor + \
            '"' + " -B " + '"' + widget.backcolor + '"' + " -g " + position + " | zsh &"
        x = x + widget.width + widget.gap
        log.Log.write(cmd)
        os.popen(cmd)


# draw right bar
drawbar(1550, action.Right)
# draw middle bar
drawbar(450, action.Middle)
# draw left bar
drawbar(10, action.Left)
