--basics
vim.opt.number = true --line numbers
vim.opt.cursorline = true --highlight line that cursor is on
vim.opt.wrap = false --disable line wrap
vim.opt.scrolloff = 10 --always keep 10 lines above/below of cursor 
vim.opt.sidescrolloff = 10 --always keep 10 lines left/right of cursor

--indentation
vim.opt.tabstop = 2 --tab width
vim.opt.shiftwidth = 2 --indent width
vim.opt.softtabstop = 2 --soft tab stop
vim.opt.expandtab = true --convert tabs to spaces
vim.opt.smartindent = true --auto indents after { and stuff
vim.opt.autoindent = true --keeps indent from current line

--search settings
vim.opt.ignorecase = true --search is case insensitive
vim.opt.smartcase = true --search is case sensitive if an upper case is used
vim.opt.hlsearch = false --doesnt highlight search results
vim.opt.incsearch = true --do search as you type

--visuals
vim.cmd.colorscheme("habamax") --set color scheme
vim.opt.termguicolors = true --use 24-bit color
vim.opt.signcolumn = "yes" --always show sign column (git,lsps)
vim.opt.showmatch = true --highlight matching bracket pairs
vim.opt.cmdheight = 1 --command line height
vim.opt.completeopt = "menuone,noinsert,noselect" --completion options, always shows menu but doesnt select one automatically
vim.opt.showmode = false --show the mode

--file handling
vim.opt.backup = false --dont create backup files
vim.opt.writebackup = false --dont create backup before writing
vim.opt.swapfile = false --dont create swapfiles
vim.opt.undofile = true --store undo history persistently
vim.opt.undodir = vim.fn.expand("~/.vim/undodir") --directory for undo file
vim.opt.updatetime = 250 --how fast things update, lower makes vim feel faster for things like completion
vim.opt.timeoutlen = 500 --key timeout duration
vim.opt.ttimeoutlen = 0 --keycode timeout
vim.opt.autoread = true --update a file if it is changed somewhere else 
vim.opt.autowrite = false --dont auto save

--behaviour
vim.opt.hidden = true --allow hidden buffers
vim.opt.errorbells = false --no error bells sound
vim.opt.backspace = "indent,eol,start" --backspace behaviour
vim.opt.autochdir = false --dont auto change directory
vim.opt.iskeyword:append("-") --treat dash as part of words 
vim.opt.path:append("**") --includes subdirectories in search
vim.opt.selection = "exclusive" --selection behaviour
vim.opt.mouse = "a" --enable mouse in all modes
vim.opt.clipboard:append("unnamedplus") --use system clipboard
vim.opt.modifiable = true --allow buffer modifications
vim.opt.encoding = "UTF-8" --set encoding

-- Command-line completion
vim.opt.wildmenu = true
vim.opt.wildmode = "longest:full,full"
vim.opt.wildignore:append({ "*.o", "*.obj", "*.pyc", "*.class", "*.jar" })

-- Better diff options
vim.opt.diffopt:append("linematch:60")

-- Performance improvements
vim.opt.redrawtime = 10000
vim.opt.maxmempattern = 20000

-- Create undo directory if it doesn't exist
local undodir = vim.fn.expand("~/.vim/undodir")
if vim.fn.isdirectory(undodir) == 0 then
  vim.fn.mkdir(undodir, "p")
end
