#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# alias ls='ls --color=auto'
# PS1='[\u@\h \W]\$ '

export PS1=" \[\e[32m\]\W\[\e[m\]  \[\e[32m\]>\[\e[m\] "
