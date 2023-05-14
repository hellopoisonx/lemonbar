#!/usr/bin/env python
class action(object):
    forecolor = "#99ccff"
    backcolor = "#000033"
    font = "ComicMonoNF-Bold"
    def __init__(self, width, cmd, gap, font = "ComicMonoNF-Bold", forecolor = "#99ccff", backcolor  = "#000033", click_event = (), click_cmd = ()):
        self.width = width
        self.cmd = cmd
        self.gap = gap
        self.font = font
        self.forecolor = forecolor
        self.backcolor = backcolor
        self.click_event = click_event
        self.click_cmd = click_cmd

start = action(0, "echo '.'", 1)
workspace = action(220, "~/lemonbar/workspace.py", 15)
clock = action(220, "~/lemonbar/clock.py", 15, click_event=(1,3), click_cmd=("kitty -e calcurse","kitty -e calcurse"))
cpu = action(90, "~/lemonbar/cpu.py", 15)
mem = action(185, "~/lemonbar/mem.py", 15)
net = action(145, "~/lemonbar/net.py", 15)
volume = action(75, "~/lemonbar/volume.py", 15, click_event=(4,5), click_cmd=("amixer sset Master 5%+", "amixer sset Master 5%-"))
window = action(180, "~/lemonbar/window.py", 15)
light = action(65, "~/lemonbar/light.py", 5, click_event=(4,5), click_cmd=("light -A 5", "light -U 5"))
#layout
Left = [workspace]
Middle = [window]
Right = [start, clock, cpu, mem, net, light, volume, start]
