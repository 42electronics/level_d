#!/bin/bash
#Installation script created by modifying Adafruit's pi-eyes.sh installer script located at
#https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/pi-eyes.sh

if [ $(id -u) -ne 0 ]; then
        echo "Installer must be run as root."
        echo "Try 'sudo bash $0'"
        exit 1
fi

clear
echo "This script modifies /boot/config.txt to force"
echo "the PWM mode on to allow for switching between"
echo "audio output on GPIO18 and PWM motor control on"
echo "GPIO12 and GPIO13. This script also adds sudo"
echo "permissions for the www-data user to access the"
echo "/usr/bin/aplay application."

echo
echo -n "CONTINUE? [y/N] "
read
if [[ ! "$REPLY" =~ ^(yes|y|Y)$ ]]; then
        echo "Canceled."
        exit 0
fi

reconfig1() {
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

reconfig2() {
        grep $2 $1 >/dev/null
        if [ $? -eq 0 ]; then
                # Pattern found; no change needed
                sed -i "s|$2|$3|g" $1 >/dev/null
                echo "www-data user found in file. $1 not updated"
        else
                echo 'www-data ALL=(ALL) NOPASSWD: /usr/bin/aplay' >> /etc/sudoers.d/RPI_Cam_Web_Interface
                echo "$1 updated"
        fi
}

reconfig1 /boot/config.txt "force_pwm_open=0"
reconfig2 /etc/sudoers.d/RPI_Cam_Web_Interface "aplay"

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
