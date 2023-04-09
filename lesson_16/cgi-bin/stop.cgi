#!/bin/bash

#motor fwd/rev as outputs
gpio -g mode 19 out
gpio -g mode 26 out
gpio -g mode 23 out
gpio -g mode 24 out

#motor enable as pwm
gpio -g mode 12 pwm
gpio -g mode 13 pwm

#motor fwd/rev all low to stop
gpio -g write 19 0 
gpio -g write 26 0
gpio -g write 23 0
gpio -g write 24 0

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo "" 
