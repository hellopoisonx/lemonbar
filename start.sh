#!/bin/sh
PIDS=$(ps -ef | rg "lemonbar -" | rg -v rg | awk '{print $2}')
if [ ${#PIDS} == 0 ]; then
  python ~/lemonbar/__init__.py
else
  killall lemonbar
fi
