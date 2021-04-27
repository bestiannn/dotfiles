#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \[\e[36m\]\W\[\e[m\]]\$ '

#my alias
alias screen='/home/bestian/.config/qtile/monitors.sh'
