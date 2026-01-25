# dotfiles-puter

<<<<<<< HEAD
this is a repo containing dotfiles for my pc and laptop

Distro: Arch

Desktop:

- pc: KDE - default kde stuff + breeze dark theme
- laptop: Sway - with swaybg, swaync, swayidle, swaylock (effects version)
  - Bar: Waybar
  - DMenu: Fuzzel
=======
this is a repo containing dotfiles for my arch pc and arch laptop

both machines are running this general setup:

Distro: Arch

WM: Sway - with swaybg, swaync, swayidle, swaylock (effects version)

Bar: Waybar

DMenu: Fuzzel
>>>>>>> a9ef0ef5787a8b6e43320407d98c527766baf8b3

Shell: ZSH (with oh-my-zsh)

Terminal: Kitty

<<<<<<< HEAD
File Explorer: Dolphin(pc) Thunar(laptop)

Browser: Firefox

Editor: Nvim

---

## Notes

---

these files are managed using stow to create symlinks to where they should actually be

shared/ is configs that are used on both machines
pc/ is the configs for kde and programs that are only used on the pc such as godot
laptop/ is the configs for sway and programs are only used on the laptop

because of how the file structure is set up to allow for this, the stow commands are a little annoying,
and cant really be done just from the main directory

bootstrap.sh is a bash script that automatically does all the stow commands,
including checking which machine it is on to do pc or laptop specific stuff

i do prefer dolphin over thunar as a file explorer but it requires all of the kde dependencies to install.
i dont have any of those on the laptop and i didnt want to use any other kde programs so i just used thunar instead
=======
File Explorer: Thunar

Browser: Firefox

***

## Notes

***

tuigreet is configured with the config file at `/etc/greetd/config.toml` which requires sudo to edit, so it has been ignored from the stow packages. I have left the `config.toml` in the `manual-configs` folder to be manually moved

these files are managed using stow, where `stow -t ~ .` stows global configs such as .config

`stow -t ~ puter` would stow the `puter` specific configs

`stow -t ~ mobile-puter` would stow the `mobile-puter` specific configs

this allows me to have different configs for things like sway on each machine whilst still keeping everything in oneplace

machine specific configs should be stowed first, then global configs afterwards 

>>>>>>> a9ef0ef5787a8b6e43320407d98c527766baf8b3
