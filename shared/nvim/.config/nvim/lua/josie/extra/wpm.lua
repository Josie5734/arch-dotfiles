--little wpm tracker

--[[
plan:

function to track wpm over given time
option to set time
default of like 30 seconds

would track character input in insert mode
count 1 word as 5 characters
ijshdf
then need function to output

--]]
--

local M = {}

local chars = {} --table to hold chars typed in insert mode

M.cpw = 5 --characters per word (how many characters count as a single word)
M.window = 10 --number of seconds to count wpm over

--calculate wpm
function M.get_wpm()
	local current = os.time() --get current time
	local count = 0 --number of characters
	for i = #chars, 1, -1 do --iterate through chars backwards
		if current - chars[i].time <= M.window then --if char is within window
			count = count + 1 --iterate counter
		else
			table.remove(chars, i) --else remove it from list
		end
	end
	return (count / M.cpw) * (60 / M.window) --output wpm
end

function M.setup()
	--define group for autocommands
	local augroup = vim.api.nvim_create_augroup("WPMGroup", { clear = true })

	vim.api.nvim_create_autocmd("InsertCharPre", {
		group = augroup,
		pattern = "*",
		callback = function()
			table.insert(chars, { char = vim.v.char, time = os.time() }) --put char and current time into table
		end,
	})

	vim.api.nvim_create_autocmd("InsertLeave", {
		group = augroup,
		pattern = "*",
		callback = function()
			print(M.get_wpm()) --print wpm
		end,
	})
end

return M
