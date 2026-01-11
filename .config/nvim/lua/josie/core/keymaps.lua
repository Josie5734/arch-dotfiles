vim.g.mapleader = " " --leader key

local keymap = vim.keymap --shorten commands

--general/misc
keymap.set('n', '<esc>', ':nohl<cr>', { desc = 'Clear Search Highlights' })

--save/exit stuff
keymap.set('n', '<leader>w', ':w<cr>', { desc = 'Save' })
keymap.set('n', '<leader>q', ':q<cr>', { desc = 'Quit' })
keymap.set('n', '<leader>x', ':x<cr>', { desc = 'Save and Quit' })

--navigation
--keymap.set('n', '<leader>e', ':Explore<cr>', { desc = 'File Explorer' })
keymap.set('n', ';', '<S-:>', { desc = 'Command Line' })

--cool number increment/decrement
keymap.set('n', '<leader>+', '<C-a>', { desc = 'Increment Number' })
keymap.set('n', '<leader>-', '<C-x>', { desc = 'Decrement Number' })

--window management
keymap.set('n', '<leader>sv', '<C-w>v', { desc = 'Split Window Vertically' }) 
keymap.set('n', '<leader>sh', '<C-w>s', { desc = 'Split Window Horizontally' })
keymap.set('n', '<leader>se', '<C-w>=', { desc = 'Make Splits Equal Size' })
keymap.set('n', '<leader>sx', '<cmd>close<cr>', { desc = 'Close Current Split' })

keymap.set("n", "<leader>to", "<cmd>tabnew<CR>", { desc = "Open new tab" }) 
keymap.set("n", "<leader>tx", "<cmd>tabclose<CR>", { desc = "Close current tab" }) 
keymap.set("n", "<leader>tn", "<cmd>tabn<CR>", { desc = "Go to next tab" })
keymap.set("n", "<leader>tp", "<cmd>tabp<CR>", { desc = "Go to previous tab" })
keymap.set("n", "<leader>tf", "<cmd>tabnew %<CR>", { desc = "Open current buffer in new tab" })
