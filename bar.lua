#!/usr/bin/env lua
local layout = require("layout")

local lemonbar = "lemonbar -p -o 1 -u 3 -f 'ComicMonoNF-Bold'-14 "

local action = function(a)
	if a == nil then
		return { "", "" }
	else
		local start = ""
		local _end = ""
		for i, item in pairs(a) do
			local click_event = "%{A" .. i .. ":" .. item .. " :}"
			start = start .. click_event
			_end = "%{A" .. i .. "}" .. _end
		end
		return { start, _end }
	end
end
-- left
local x = 10
for _, item in ipairs(layout.left) do
	local cmd = lemonbar
		.. "-g "
		.. item.length
		.. "x"
		.. "27"
		.. "+"
		.. x
		.. "+"
		.. "1"
		.. " -F '#"
		.. item.color.foreground
		.. "' -B '#"
		.. item.color.background
		.. "'"
		.. " | zsh &"
	cmd = '(while true\n do\n echo "'
		.. action(item.action)[1]
		.. "$("
		.. item.stdout
		.. ")"
		.. action(item.action)[2]
		.. '";sleep ' ..item.interval.. 's;\ndone)| '
		.. cmd
	print(cmd)
	os.execute(cmd)
	x = x + item.length + item.gap
end
