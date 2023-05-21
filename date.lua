#!/usr/bin/env lua
local date = require("widgets").date

print(date.cmd())
os.execute("sleep " .. date.interval .. "s")
