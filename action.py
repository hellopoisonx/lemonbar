#!/usr/bin/env python
class action(object):
    forecolor = "#99ccff"
    backcolor = "#000033"
    font = "JetBrainsMonoNLNerdFont"
    def __init__(self, width, cmd, gap, font = "JetBrainsMonoNLNerdFont", forecolor = "#99ccff", backcolor  = "#000033"):
        self.width = width
        self.cmd = cmd
        self.gap = gap
        self.font = font
        self.forecolor = forecolor
        self.backcolor = backcolor

workspace_current = action(30, "~/lemonbar/workspace.py", 15)
workspace_all = action(230, "~/lemonbar/workspace_all.py", 15)
clock_hour = action(90, "~/lemonbar/clock_hour.py", 15)
clock_year = action(160, "~/lemonbar/clock_year.py", 15)
cpu = action(85, "~/lemonbar/cpu.py", 15)
mem = action(180, "~/lemonbar/mem.py", 15)
net = action(175, "~/lemonbar/net.py", 15)
volume = action(90, "~/lemonbar/volume.py", 15)

Left = [workspace_current, workspace_all]
Right = [clock_year, clock_hour, cpu, mem, net, volume]
