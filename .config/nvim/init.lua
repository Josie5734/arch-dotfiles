--basic settings
vim.o.number = true --numbered lines
vim.o.wrap = false --line wrapping false
vim.o.tabstop = 4 --tab size
vim.o.swapfile = false --disable swapfiles



--basic keybinds
vim.g.mapleader = " " --set leader key

vim.keymap.set('n', '<leader>w', ':w<CR>') --write
vim.keymap.set('n', '<leader>q', ':q<CR>') --quit
vim.keymap.set('n', '<leader>x', ':x<CR>') --save and quit

vim.keymap.set('n', '<leader>e', ':Ex<CR>') --file explorer

vim.keymap.set('n', '<leader>o', ':update<CR> :source<CR>') --write if changed, source file



--plugins
vim.pack.add({
		{src = "https://github.com/vague-theme/vague.nvim"},
})

require("vague").setup({})

vim.cmd("colorscheme vague")
