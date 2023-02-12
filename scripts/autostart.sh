picom &
setxkbmap -model abnt2 -layout br -variant abnt2
nitrogen --restore &
# tint2 -c $HOME/.config/tint2/custom_left.tint2rc &
# tint2 -c $HOME/.config/tint2/custom_center.tint2rc &
# tint2 -c $HOME/.config/tint2/custom_right.tint2rc &
/usr/bin/numlockx on &
# $HOME/.config/polybar/launch.sh &
# volumeicon &
# quicktile --daemonize &
~/scripts/ssh-startup.sh &

conky -c /home/vinicius/.conkyrc &

eww open bar
plank &
firefox &
discord &
kitty &
telegram-desktop &
# xfce4-power-manager & 
spotify --force-device-scale-factor=1.8 %U &

sleep 20

wmctrl -r kitty -t 1
wmctrl -r discord -t 3
wmctrl -r firefox -t 0
wmctrl -r telegram-desktop -t 2
wmctrl -r TelegramDesktop -t 2
wmctrl -r spotify -t 2
# wmctrl -a kitty

# picom &
# sleep 5
# kitty &
# plank &

# $HOME/.config/polybar/launch.sh &

eww -c ~/.config/eww/Bar/ open --toggle panel
