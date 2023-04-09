#!/bin/bash

#right motor speed
gpio -g pwm 12 850

#left motor speed
gpio -g pwm 13 850

#right motor reverse
gpio -g write 23 1

#left motor forward
gpio -g write 19 1

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
