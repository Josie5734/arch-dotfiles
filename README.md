# Arch Dotfiles

this is a repo containing dotfiles for my pc and laptop

Distro: Arch

Desktop:

- pc: KDE - default kde stuff + breeze dark theme
- laptop: Sway - with swaybg, swaync, swayidle, swaylock (effects version)
  - Bar: Waybar
  - DMenu: Fuzzel

Shell: ZSH (with oh-my-zsh)

Terminal: Kitty

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
