#!/usr/bin/env python
class action(object):
    forecolor = "#99ccff"
    backcolor = "#000033"
    font = "ComicMonoNF-Bold"
    def __init__(self, width, cmd, gap, font = "ComicMonoNF-Bold", forecolor = "#99ccff", backcolor  = "#000033"):
        self.width = width
        self.cmd = cmd
        self.gap = gap
        self.font = font
        self.forecolor = forecolor
        self.backcolor = backcolor

start = action(0, "echo '.'", 1)
workspace = action(225, "~/lemonbar/workspace.py", 15)
clock = action(220, "~/lemonbar/clock.py", 15)
cpu = action(90, "~/lemonbar/cpu.py", 15)
mem = action(185, "~/lemonbar/mem.py", 15)
net = action(145, "~/lemonbar/net.py", 15)
volume = action(75, "~/lemonbar/volume.py", 15)

Left = [workspace]
Right = [start, start, clock, cpu, mem, net, volume, start]
