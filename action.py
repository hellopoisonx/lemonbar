#!/usr/bin/env python
import os

Lemonbar_root = "/home/hpxx/lemonbar/"


class action(object):
    forecolor = "#99ccff"
    backcolor = "#000033"
    font = "ComicMonoNF-Bold"

    def __init__(self, width, cmd, gap, font="ComicMonoNF-Bold", forecolor="#99ccff", backcolor="#000033", click_event=(), click_cmd=(), interval=0.5):
        self.width = width
        self.cmd = cmd
        self.gap = gap
        self.font = font
        self.forecolor = forecolor
        self.backcolor = backcolor
        self.click_event = click_event  # 1,2,3,4,5:left,middle,right,up,down
        self.click_cmd = click_cmd  # foo,foo
        self.interval = interval


start = action(0, "echo '.'", 1)
workspace = action(int((os.popen("xdotool get_num_desktops").read())) * 22, "~/lemonbar/workspace.py", 15, interval=0.2)
clock = action(220, "~/lemonbar/clock.py", 15, click_event=(1, 3),
               click_cmd=("alacritty -e calcurse", "alacritty -e calcurse"), interval=40)
cpu = action(90, "~/lemonbar/cpu.py", 15)
mem = action(185, "~/lemonbar/mem.py", 15, interval=2)
net = action(280, "~/lemonbar/net.py", 20, interval=1)
volume = action(75, "~/lemonbar/volume.py", 15, click_event=(4, 5),
                click_cmd=("amixer sset Master 5%+", "amixer sset Master 5%-"))
window = action(300, "~/lemonbar/window.py", 15, font="wqy-zenhei")
light = action(65, "~/lemonbar/light.py", 5, click_event=(4, 5),
               click_cmd=("light -A 5", "light -U 5"),)
music = action(300, "~/lemonbar/music.py", 10, font="wqy-zenhei", interval=2)

# layout
Left = [workspace]
Middle = [window, music]
Right = [start, clock, cpu, mem, net, light, volume, start]
