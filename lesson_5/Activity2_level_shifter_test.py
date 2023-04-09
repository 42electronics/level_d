#Copyright (c) 2023 42 Development dba 42 Electronics
#Author: Eric Feickert
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in the
#Software without restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
#Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import RPi.GPIO as GPIO
import time

pins = [4, 17, 27, 22, 21]
r_line = 4
r_obs = 17
l_line = 27
l_obs = 22
echo = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(r_line) == True:
            print('Right Line Sensor High')
        elif GPIO.input(r_obs) == True:
            print('Right Obstacle Sensor High')
        elif GPIO.input(l_line) == True:
            print('Left Line Sensor High')
        elif GPIO.input(l_obs) == True:
            print('Left Obstacle Sensor High')
        elif GPIO.input(echo) == True:
            print('Echo High')
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()