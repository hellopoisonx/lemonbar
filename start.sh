#!/bin/sh
PIDS=$(ps -ef | rg "lemonbar -" | rg -v rg | awk '{print $2}')
if [ ${#PIDS} == 0 ]; then
  lua ~/lemonbar_lua/bar.lua
else
  killall lemonbar
fi
