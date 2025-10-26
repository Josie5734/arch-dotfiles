--basic settings (mostly for lines) (needs to be separated out at some point)
vim.o.number = true             --numbered lines
vim.o.wrap = false              --line wrapping false
vim.o.tabstop = 4               --tab size
vim.o.shiftwidth = 4            --the autoindent to do (eg after (if) statement)
vim.o.swapfile = false          --disable swapfiles
vim.o.signcolumn = "yes"        --sign column
vim.o.winborder = "rounded"     --add borders for hovering on text - mapped to (K)
vim.o.cursorline = true         --highlight current line that cursor is on
vim.o.scrolloff = 10            --keep 10 lines above/below cursor
vim.o.sidescrolloff = 10        --keep 10 lines to left/right of cursor
vim.o.showmatch = true          --show matching bracket pair
vim.o.autoread = true           --update file if it is changed from another location
vim.o.clipboard = "unnamedplus" --use system clipboard



--basic keybinds
vim.g.mapleader = " "                                                                 --set leader key

vim.keymap.set('n', '<leader>w', ':w<CR>', { desc = "Write file" })                   --write
vim.keymap.set('n', '<leader>q', ':q<CR>', { desc = "Quit" })                         --quit
vim.keymap.set('n', '<leader>x', ':x<CR>', { desc = "Save and Quit" })                --save and quit
vim.keymap.set('n', '<leader>o', ':update<CR> :source<CR>', { desc = "source file" }) --write if changed, source file

vim.keymap.set({ 'n', 'v', 'x' }, '<leader>y', '"+y<CR>')                             --yank to system clipboard
vim.keymap.set({ 'n', 'v', 'x' }, '<leader>p', '"+p<CR>')                             --paste from system clipboard

vim.keymap.set('n', '<leader>e', ':Oil<CR>', { desc = "Oil File Explorer" })          --file explorer

--split buffer/tab keybinds
-- Buffer navigation
vim.keymap.set("n", "<leader>bn", ":bnext<CR>", { desc = "Next buffer" })
vim.keymap.set("n", "<leader>bp", ":bprevious<CR>", { desc = "Previous buffer" })

-- Better window navigation
vim.keymap.set("n", "<C-h>", "<C-w>h", { desc = "Move to left window" })
vim.keymap.set("n", "<C-j>", "<C-w>j", { desc = "Move to bottom window" })
vim.keymap.set("n", "<C-k>", "<C-w>k", { desc = "Move to top window" })
vim.keymap.set("n", "<C-l>", "<C-w>l", { desc = "Move to right window" })

-- Splitting & Resizing
vim.keymap.set("n", "<leader>sv", ":vsplit<CR>", { desc = "Split window vertically" })
vim.keymap.set("n", "<leader>sh", ":split<CR>", { desc = "Split window horizontally" })
vim.keymap.set("n", "<C-Up>", ":resize +2<CR>", { desc = "Increase window height" })
vim.keymap.set("n", "<C-Down>", ":resize -2<CR>", { desc = "Decrease window height" })
vim.keymap.set("n", "<C-Left>", ":vertical resize -2<CR>", { desc = "Decrease window width" })
vim.keymap.set("n", "<C-Right>", ":vertical resize +2<CR>", { desc = "Increase window width" })



--plugins
vim.pack.add({                                         --install plugins list
	{ src = "https://github.com/catppuccin/nvim" },    --colorscheme
	{ src = "https://github.com/mason-org/mason.nvim" }, --mason for auto install lsps
	{ src = "https://github.com/neovim/nvim-lspconfig" }, --auto provide lsp configs
	{ src = "https://github.com/stevearc/oil.nvim" },  --oil
	{ src = "https://github.com/folke/which-key.nvim" }, --which key finder
	--modules from the "mini" set of neovim plugins
	{ src = "https://github.com/nvim-mini/mini.pick" }, --file finder
	{ src = "https://github.com/nvim-mini/mini.pairs" }, --auto bracket pairs
	{ src = "https://github.com/nvim-mini/mini-git" }, --git integration
})

--plugin setups
vim.cmd.colorscheme "catppuccin-mocha" --set catppuccin theme
require("mini.pick").setup()           --mini pick setup
require("mini.pairs").setup()          --mini pairs setup
require("mini.git").setup()            --mini git setup
require("oil").setup()                 --oil setup

--lsps
require("mason").setup()                --setup mason
vim.lsp.enable({ "lua_ls", "pyright" }) --enable lsps

--plugin keybinds
vim.keymap.set('n', '<leader>lf', vim.lsp.buf.format, { desc = "Language Format" }) --language format
vim.keymap.set('n', '<leader>f', ':Pick files<CR>', { desc = "Pick file search" })  --pick file finder
