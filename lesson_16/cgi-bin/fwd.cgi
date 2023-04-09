#!/bin/bash

#right motor speed
gpio -g pwm 12 1000

#left motor speed
gpio -g pwm 13 1000

#right motor forward
gpio -g write 24 1 

#left motor forward
gpio -g write 19 1 

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
 
