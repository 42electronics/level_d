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

motors = [13,19,26,12,23,24]
r_enable = 12
r_for = 24
r_rev = 23
l_enable = 13
l_for = 19
l_rev = 26
l_line = 27
r_line = 4
obs_right = 17
end = 0
motor_fast = 60
motor_slow = 30

GPIO.setmode(GPIO.BCM)
GPIO.setup(motors, GPIO.OUT)
GPIO.setup(l_line, GPIO.IN)
GPIO.setup(r_line, GPIO.IN)
GPIO.setup(obs_right, GPIO.IN)

l_pwm = GPIO.PWM(l_enable, 1000)
l_pwm.start(motor_fast)
r_pwm = GPIO.PWM(r_enable, 1000)
r_pwm.start(motor_fast)

try:
    while end == 0:
        while GPIO.input(l_line) == False:
            r_pwm.ChangeDutyCycle(motor_slow)
            GPIO.output(l_for, 0)
            GPIO.output(l_rev, 1)
            time.sleep(0.01)
        while GPIO.input(r_line) == False:
            l_pwm.ChangeDutyCycle(motor_slow)
            GPIO.output(r_for, 0)
            GPIO.output(r_rev, 1)
            time.sleep(0.01)
        if GPIO.input(obs_right) == False:
            GPIO.output(r_for, 0)
            GPIO.output(l_for, 0)
            GPIO.output(r_rev, 0)
            GPIO.output(l_rev, 0)
            print('Shutdown')
            end = 1
        else:
            r_pwm.ChangeDutyCycle(motor_fast)
            l_pwm.ChangeDutyCycle(motor_fast)
            GPIO.output(l_rev, 0)
            GPIO.output(r_rev, 0)
            GPIO.output(l_for, 1)
            GPIO.output(r_for, 1)
finally:
    GPIO.cleanup()