#!/bin/bash
#Installation script created by modifying Adafruit's pi-eyes.sh installer scrip$
#https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/mast$

if [ $(id -u) -ne 0 ]; then
        echo "Installer must be run as root."
        echo "Try 'sudo bash $0'"
        exit 1
fi

clear
echo "This script adds a line to the end of the"
echo "/boot/config.txt file that forces the PWM"
echo "mode on to allow for switching between audio"
echo "output on GPIO18 and PWM motor control on"
echo "GPIO12 and GPIO13"

echo
echo -n "CONTINUE? [y/N] "
read
if [[ ! "$REPLY" =~ ^(yes|y|Y)$ ]]; then
        echo "Canceled."
        exit 0
fi

reconfig() {
        grep $2 $1 >/dev/null
        if [ $? -eq 0 ]; then
                # Pattern found; no change needed
                sed -i "s|$2|$3|g" $1 >/dev/null
                echo "PWM command found in file. $1 not updated"
        else
                echo 'force_pwm_open=0' >> /boot/config.txt
                echo "$1 updated"
        fi
}

reconfig /boot/config.txt "force_pwm_open=0"

# PROMPT FOR REBOOT --------------------------------------------------------

echo "Done."
echo
echo "Settings take effect on next boot."
echo
echo -n "REBOOT NOW? [y/N] "
read
if [[ ! "$REPLY" =~ ^(yes|y|Y)$ ]]; then
        echo "Exiting without reboot."
        exit 0
fi
echo "Reboot started..."
reboot
exit 0

