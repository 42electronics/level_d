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

trigger = 20
echo = 21

motors = [12, 24, 23, 13, 19, 26]
r_enable = 12
r_for = 24
r_rev = 23
l_enable = 13
l_for = 19
l_rev = 26

obs_left = 22
obs_right = 17

r_speed = 60
l_speed = 60
turn_delay = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(motors, GPIO.OUT)
GPIO.setup(obs_left, GPIO.IN)
GPIO.setup(obs_right, GPIO.IN)

r_pwm = GPIO.PWM(r_enable, 1000)
r_pwm.start(r_speed)
l_pwm = GPIO.PWM(l_enable, 1000)
l_pwm.start(l_speed)

def range_check():
	GPIO.output(trigger, True)
	time.sleep(0.00001)
	GPIO.output(trigger, False)

	while GPIO.input(echo) == False:
		start_timer = time.time()

	while GPIO.input(echo) == True:
		stop_timer = time.time()

	elapsed_time = stop_timer-start_timer
	distance = (elapsed_time * 34300)/2
	return distance

def stop():
	GPIO.output(r_for, 0)
	GPIO.output(l_for, 0)
	GPIO.output(r_rev, 0)
	GPIO.output(l_rev, 0)
	time.sleep(0.1)

def reverse():
	stop()
	GPIO.output(r_rev, 1)
	GPIO.output(l_rev, 1)
	time.sleep(0.5)
	stop()

try:
	while True:
		distance = range_check()
		if distance <= 10:
			stop()
			print('Emergency Stop!')
			raise SystemExit()
		elif 10 < distance < 20:
			reverse()
			GPIO.output(r_for, 1)
			GPIO.output(l_rev, 1)
			time.sleep(turn_delay)
			stop()
		elif GPIO.input(obs_right) == False:
			reverse()
			GPIO.output(r_for, 1)
			GPIO.output(l_rev, 1)
			time.sleep(turn_delay)
			stop()
		elif GPIO.input(obs_left) == False:
			reverse()
			GPIO.output(r_rev, 1)
			GPIO.output(l_for, 1)
			time.sleep(turn_delay)
			stop()
		else:
			GPIO.output(r_for, 1)
			GPIO.output(l_for, 1)
			time.sleep(0.05)

except (KeyboardInterrupt, SystemExit):
	stop()
	GPIO.cleanup()