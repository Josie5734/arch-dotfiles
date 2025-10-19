# dotfiles-puter

***

this is a repo containing dotfiles for my arch pc and arch laptop

both machines are running this general setup:

Distro: Arch
WM: Sway - with swaybg, swaync, swayidle, swaylock
Bar: Waybar
DMenu: Fuzzel
Shell: ZSH (with oh-my-zsh)
Terminal: Kitty
File Explorer: Thunar
Browser: Firefox

***

### notes

***

tuigreet is configured with the config file at `/etc/greetd/config.toml` which requires sudo to edit. I have left the `config.toml` in the `manual-configs` folder 

these files are managed using stow, where `stow -t ~ .` stows global configs such as .config
`stow -t ~ puter` would stow the `puter` specific configs
`stow -t ~ mobile-puter` would stow the `mobile-puter` specific configs

this allows me to have different configs for things like sway on each machine whilst still keeping everything in oneplace

