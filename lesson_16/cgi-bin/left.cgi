#!/bin/bash

#right motor speed
gpio -g pwm 12 850

#left motor speed
gpio -g pwm 13 850

#right motor forward
gpio -g write 24 1

#left motor reverse
gpio -g write 26 1

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
