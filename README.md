# arch dotfiles

These are (some of) my dotfiles for my Arch Linux + Hyprland setup. This repo works with GNU Stow to keep a version controlled backup of my config files that I can redownload/rollback on whenever I need.

### Info

- OS: Arch Linux
- WM: Hyprland
- Terminal: Kitty + ZSH
- Editor: Zeditor + Nvim
- Browser: Firefox
- File Browser: Yazi + Thunar


### Hyprland setup

- most utils use a Hypr native package such as HyprShot, HyprIdle, HyprLock etc
- Bar: Ashell (Currently, may be changed soon)
- Launcher: Fuzzel


### Usage

- ```git clone``` this repo somewhere in your $HOME directory (for the stow symlink paths to work)
- To use these dotfiles, all packages listed in ```pkglist.txt``` must be installed via ```pacman -S --needed < pkglist.txt```
- GNU Stow must also be installed to symlink the files into the right directories by running ```stow .``` from the repo root. Alternatively, individual files can be copied/stowed manually or with stow
