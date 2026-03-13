--wpm tracker
wpm = require("josie.extra.wpm")
wpm.setup()

--neostats
vim.opt.runtimepath:prepend("~/programming/nvim/plugins/neostats") --add plugin folder to path
neostats = require("neostats")
neostats.setup()
