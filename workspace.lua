#!/usr/bin/env lua
local ws = require("widgets")

print(ws.workspace.cmd())
os.execute("sleep " .. tostring(ws.workspace.interval) .. "s")
