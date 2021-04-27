#!/bin/bash

if [[ $1 -eq 1 ]]
then
  xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-1-1 --off
elif [[ $1 -eq 2 ]]
then
  xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x8 --rotate normal --output HDMI-1-1 --mode 1366x768 --pos 1920x0 --rotate normal
else
  echo "EROR 404"
fi
