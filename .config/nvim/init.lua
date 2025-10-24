--basic settings
vim.o.number = true         --numbered lines
vim.o.wrap = false          --line wrapping false
vim.o.tabstop = 4           --tab size
vim.o.swapfile = false      --disable swapfiles
vim.o.signcolumn = "yes"    --sign column
vim.o.winborder = "rounded" --add borders for hovering on text - mapped to (K)



--basic keybinds
vim.g.mapleader = " "                      --set leader key

vim.keymap.set('n', '<leader>w', ':w<CR>') --write
vim.keymap.set('n', '<leader>q', ':q<CR>') --quit
vim.keymap.set('n', '<leader>x', ':x<CR>') --save and quit

vim.keymap.set({ 'n', 'v', 'x' }, '<leader>y', '"+y<CR>') --yank to system clipboard
vim.keymap.set({ 'n', 'v', 'x' }, '<leader>p', '"+p<CR>') --paste from system clipboard

vim.keymap.set('n', '<leader>e', ':Oil<CR>')                --file explorer

vim.keymap.set('n', '<leader>o', ':update<CR> :source<CR>') --write if changed, source file



--plugins

--install list
vim.pack.add({
	{ src = "https://github.com/catppuccin/nvim" }, --colorscheme
	{ src = "https://github.com/mason-org/mason.nvim" }, --mason for auto install lsps
	{ src = "https://github.com/neovim/nvim-lspconfig" }, --auto provide lsp configs
	{ src = "https://github.com/nvim-mini/mini.pick" }, --mini pick file finder
	{ src = "https://github.com/stevearc/oil.nvim" }, --oil
})

--plugin setups
vim.cmd.colorscheme "catppuccin-mocha" --set catppuccin theme
require("mini.pick").setup()           --mini pick setup
require("oil").setup()                 --oil setup

--lsps
require("mason").setup()     --setup mason
vim.lsp.enable({ "lua_ls" }) --enable lsps


--plugin keybinds
vim.keymap.set('n', '<leader>lf', vim.lsp.buf.format) --language format
vim.keymap.set('n', '<leader>f', ':Pick files<CR>')   --pick file finder
