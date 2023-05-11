#!/usr/bin/env python
import os
import time
# position = ["350+333+2", "80+720+2", "182x26+820+2", "155x26+1120+2", "120x26+1350+2"]
# lemonbar = "lemonbar -d -p -f 'JetBrainsMonoNLNerdFont' -f 'Font Awesome 6 Free' -B '#1a1a1a' -F '#4d94ff' -g "
# interval = "2s"
# x = 20
def get_all_workspace():
    return " 1 2 3 4 5 6 7 8 9"
def get_current_workspace():
    current_workspace = int(os.popen("xdotool get_desktop").read()) + 1
    return " " + str(current_workspace).rstrip('\n')
def get_net_rate():
    """ """
    down_before = float(os.popen("cat /proc/net/dev | grep wlp3s0 | awk   '{printf $2}'").read())
    time.sleep(1)
    down_after = float(os.popen("cat /proc/net/dev | grep wlp3s0 | awk   '{printf $2}'").read())
    down = (down_after - down_before) / 1024 / 1024
    return " " + "\uf0ed" + str(":{0}MB/s".format("%.2f"%down))
def get_volume():
    """ """
    volume = str(os.popen("amixer get Master | tail -n1 ").read())
    first = volume.find('[')
    end = volume.find(']')
    return " " + volume[first:end+1]

def clock_year():
    """ """
    return time.strftime(" %Y-%m-%d", time.localtime())
def clock_hour():
    return time.strftime(" %H:%M", time.localtime()) 
def get_memory():
    """ """
    mem_free = round(int(os.popen("grep  'MemAvailable:' /proc/meminfo | awk '{print $2}'").read()) / 1024 /1024, 1)
    mem_total = round(int(os.popen("grep  'MemTotal:' /proc/meminfo | awk '{print $2}'").read()) /1024 / 1024, 1)
    mem_used = round(mem_total - mem_free, 1)
    return " " + str(mem_used) + 'GB/' + str(mem_total) + 'GB'

def get_cpu():
    """ """
    cpu_usage = str(os.popen("top -bn1 | grep 'Cpu(s)' | awk '{print $2}'").read()).rstrip('\n')
    return " " + cpu_usage + "%"
