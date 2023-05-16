#!/usr/bin/env python
import os
import time
# position = ["350+333+2", "80+720+2", "182x26+820+2", "155x26+1120+2", "120x26+1350+2"]
# lemonbar = "lemonbar -d -p -f 'JetBrainsMonoNLNerdFont' -f 'Font Awesome 6 Free' -B '#1a1a1a' -F '#4d94ff' -g "
# interval = "2s"
# x = 20
def get_current_workspace():
    workspace = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_workspace = int(os.popen("xdotool get_desktop").read())
    workspace[current_workspace] = "%{F#cc99ff}%{+u}" + str(current_workspace + 1) + "%{-u}%{F}"
    result = " "
    for i in workspace:
        result += i + " "
    return "%{c}" + result.rstrip('\n') + "%{c}"
def get_widow_name():
    window_name = os.popen("xprop -id $(xprop -root _NET_ACTIVE_WINDOW | cut -d ' ' -f 5) WM_CLASS").read()
    window_name = window_name[window_name.find("\"",window_name.find("\"") + 1) + 4: -2]
    return "%{c}" + window_name + "%{c}"
def get_net_rate():
    """ """
    down_before = float(os.popen("cat /proc/net/dev | grep wlp3s0 | awk   '{printf $2}'").read())
    up_before = float(os.popen("cat /proc/net/dev | rg wlp3s0 | awk '{print $10}'").read())
    time.sleep(1)
    down_after = float(os.popen("cat /proc/net/dev | grep wlp3s0 | awk   '{printf $2}'").read())
    up_after = float(os.popen("cat /proc/net/dev | rg wlp3s0 | awk '{print $10}'").read())
    down = (down_after - down_before) / 1024 / 1024
    up = (up_after - up_before) / 1024 / 1024
    return "%{c}" + "\uf0ed" + str(":{0}MB/s ".format("%.2f"%down)) + "\uf0ee" + str(":{0}MB/s".format("%.2f"%up)) + "%{c}"
def get_volume():
    """ """
    volume_get = str(os.popen("amixer get Master | tail -n1 ").read())
    first = volume_get.find('[')
    end = volume_get.find(']')
    volume = int(volume_get[first+1:end-1])
    if volume <= 34:
       return " \uf027" + str(volume) + "%"
    return "\uf028" + str(volume) 

def clock():
    year_month_day = time.strftime("%Y-%m-%d", time.localtime())
    hour_minute = time.strftime("%H:%M", time.localtime()) 
    return " \uf073" + year_month_day + " " + hour_minute + " "
def get_memory():
    """ """
    mem_free = round(int(os.popen("grep  'MemAvailable:' /proc/meminfo | awk '{print $2}'").read()) / 1024 /1024, 1)
    mem_total = round(int(os.popen("grep  'MemTotal:' /proc/meminfo | awk '{print $2}'").read()) /1024 / 1024, 1)
    mem_used = round(mem_total - mem_free, 1)
    return " %{c}\uf4bc" + str(mem_used) + 'GB/' + str(mem_total) + 'GB%{c}'

def get_cpu():
    """ """
    cpu_usage = str(os.popen("top -bn1 | grep 'Cpu(s)' | awk '{print $2}'").read()).rstrip('\n')
    return " %{c}\uf2db" + cpu_usage + "%%%{c}"

def get_light():
    """ """
    light = str(int(float(os.popen("light").read().rstrip('\n'))))
    return " \uf0eb" + light 
