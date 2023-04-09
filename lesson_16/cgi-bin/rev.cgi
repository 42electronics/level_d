#!/bin/bash

#right motor speed
gpio -g pwm 12 1000

#left motor speed
gpio -g pwm 13 1000

#right motor reverse
gpio -g write 23 1

#left motor reverse
gpio -g write 26 1

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
