#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# alias ls='ls --color=auto'
# PS1='[\u@\h \W]\$ '

PS1=' \[\e[0;91m\]愛 \[\e[0m\]\W \[\e[0;96m\]> \[\e[0m\]'

alias clock='sudo sudo ntpd -qg && sudo hwclock --systohc'
