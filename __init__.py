#!/usr/bin/env python
import os
workspace_total = "1 2 3 4 5"
widgets = ["workspace", "show_all_workspace", "clock_hour", "clock_year", "cpu", "net", "volume", "mem"]
lemonbar = "lemonbar -d -p -o 1 -f 'JetBrainsMonoNLNerdFont'-12 -f 'Font Awesome 6 Free' -B '#1a1a1a' -F '#4d94ff' -g "
x = 20
os.popen("killall lemonbar")
for i in range(0, 8):
    x = 20
    position = "160" + "x" + "27" + "+" + str(x * i) + "1"
    if widgets[i] == "show_all_workspace":
        x = 9
        os.popen("echo " + workspace_total + " | " + lemonbar + position + " &")
        continue
    if widgets[i] == "workspace":
        position = "30" + "x" + "27" + "+" + str(x * i) + "0"
    if widgets[i] == "cpu" or widgets[i] == "volume":
        position = "80" + "x" + "27" + "+" + str(x * i) + "0"
        x = 9
    os.popen("/home/hpxx/dwm2/script/lemonbar/" + widgets[i] + ".py" + " | " + lemonbar + position + " &")
