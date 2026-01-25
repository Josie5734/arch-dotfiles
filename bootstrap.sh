#!/bin/bash

# stow shared dotfiles
cd shared
stow -t ~ kitty
stow -t ~ nvim
stow -t ~ zsh


# get whether on pc or laptop 
hostname="$(hostnamectl --static)"
pc="puter"
laptop="mobile-puter"

# stow platform specific files
if [ "$hostname" = "$pc" ]; then
  # stow pc files 
  cd pc
  stow --adopt -t ~ system
  stow --adopt -t ~ desktop
  cd ..
elif [ "$hostname" = "$laptop" ]; then
  # stow laptop files 
  cd laptop 
  stow --adopt -t ~ system
  stow --adopt -t ~ desktop
  cd ..
else
  # give error
  echo "not on the intended systems"
  echo "edit script to fix"
fi
