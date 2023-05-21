#!/usr/bin/env lua
local col = require("color.color")
local widgets = {}
local lemonbar_root = "/home/hpxx/lemonbar_lua/"
widgets.workspace = {
	color = {
		foreground = col.light_blue,
		background = col.dark_blue,
	},
	action = nil,
	cmd = function()
		local workspace = " "
		local nums = io.popen("xdotool get_num_desktops"):read("n")
		for i = 1, nums do
			local current = io.popen("xdotool get_desktop"):read("n") + 1
			if i == current then
				workspace = workspace .. "%{F#" .. col.pink .. "}%{+u}" .. tostring(current) .. "%{-u}%{F} "
			else
				workspace = workspace .. tostring(i) .. " "
			end
		end
		return workspace
	end,
	stdout = lemonbar_root .. "workspace.lua",
	interval = 0.5,
	gap = 15,
	length = 220,
}
widgets.date = {
	color = widgets.workspace.color,
	action = nil,
	cmd = function()
		local date = string.gsub(io.popen("LANG=en_US date +%a-%b-%d"):read("a"), "\n", "")
		return "%{c}" .. date .. "%{c}"
	end,
	stdout = lemonbar_root .. "date.lua",
	interval = 0.5,
	gap = 5,
	length = 150,
}
widgets.time = {
	color = widgets.workspace.color,
	action = nil,
	cmd = function()
		local time = string.gsub(io.popen("LANG=en_US date +%H:%M"):read("a"), "\n", "")
		return "%{c}" .. time .. "%{c}"
	end,
	stdout = lemonbar_root .. "time.lua",
	interval = 2,
	gap = 5,
	length = 120,
}
widgets.volume = {
	color = widgets.workspace.color,
	action = {
		[4] = "amixer sset Master 5%+",
		[5] = "amixer sset Master 5%-",
	},
	cmd = function()
		local volume = io.popen("amixer get Master | tail -n1"):read("a")
		local before, _ = string.find(volume, "[", 1, true)
		local after, _ = string.find(volume, "]", 1, true)
		volume = string.sub(volume, before + 1, after - 2)
		return "" .. volume .. ""
	end,
	stdout = lemonbar_root .. "volume.lua",
	interval = 0.5,
	gap = 5,
	length = 60,
}
widgets.light = {
	color = widgets.workspace.color,
	action = {
		[4] = "light -A 5",
		[5] = "light -U 5",
	},
	cmd = function()
        local light = io.popen("light"):read("n")
		return "" .. light .. ""
	end,
	stdout = lemonbar_root .. "light.lua",
	interval = 0.5,
	gap = 5,
	length = 60,
}
return widgets
