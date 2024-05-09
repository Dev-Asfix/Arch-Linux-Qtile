#!/bin/sh

#configuracion teclado español
setxkbmap la-latin1 &

#resolucion de la resolucion
xrandr --output eDP1 --primary --mode 1366x768 --pos 0x0 --rotate normal --output DP1 --mode 1280x768 --pos 0x0 --rotate normal --output HDMI1 --off --output HDMI2 --off --output VIRTUAL1 --off

#iconos del sistema

udiskie -t &
nm-applet &
volumeicon &
cbatticon -u 5 &

nitrogen --restore &

#Configuracion de Doble Pantalla 
xrandr --output DP1 --mode 1600x900 --right-of eDP1


