#!/usr/bin/env lua
local time = require("widgets").time

print(time.cmd())
os.execute("sleep " .. time.interval .. "s")
