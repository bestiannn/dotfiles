#!/bin/sh
#xrandr --output eDP1 --primary --mode 1920x1080 --rotate normal --output HDMI1 --mode 1366x768 --rotate normal --right-of eDP1
xrandr --output eDP-1 --primary --mode 1920x1080 --rotate normal --output HDMI-1 --mode 1366x768 --rotate normal --right-of eDP-1

nm-applet &
nitrogen --restore &
numlockx &
dunst &
picom &