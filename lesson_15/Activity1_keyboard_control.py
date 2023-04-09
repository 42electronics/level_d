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

from tkinter import Tk
import RPi.GPIO as GPIO

motors = [13,19,26,12,23,24]
r_enable = 12
r_for = 24
r_rev = 23
l_enable = 13
l_for = 19
l_rev = 26
r_fast = 80
l_fast = 80
r_slow = 40
l_slow = 40

GPIO.setmode(GPIO.BCM)
GPIO.setup(motors, GPIO.OUT)
GPIO.output(motors, GPIO.LOW)
pwm_right = GPIO.PWM(r_enable, 1000)
pwm_left = GPIO.PWM(l_enable, 1000)
pwm_right.start(r_fast)
pwm_left.start(l_fast)

def on_close():
 	print('Quitting Program...')
 	GPIO.cleanup()
 	root.destroy()

def up_arrow(event):
 	pwm_right.ChangeDutyCycle(r_fast)
 	pwm_left.ChangeDutyCycle(l_fast)
 	GPIO.output(r_rev, 0)
 	GPIO.output(r_for, 1)
 	GPIO.output(l_rev, 0)
 	GPIO.output(l_for, 1)

def down_arrow(event):
 	pwm_right.ChangeDutyCycle(r_fast)
 	pwm_left.ChangeDutyCycle(l_fast)
 	GPIO.output(r_rev, 1)
 	GPIO.output(r_for, 0)
 	GPIO.output(l_rev, 1)
 	GPIO.output(l_for, 0)

def left_arrow(event):
 	pwm_right.ChangeDutyCycle(r_slow)
 	pwm_left.ChangeDutyCycle(l_slow)
 	GPIO.output(r_rev, 0)
 	GPIO.output(r_for, 1)
 	GPIO.output(l_rev, 1)
 	GPIO.output(l_for, 0)

def right_arrow(event):
 	pwm_right.ChangeDutyCycle(r_slow)
 	pwm_left.ChangeDutyCycle(l_slow)
 	GPIO.output(r_rev, 1)
 	GPIO.output(r_for, 0)
 	GPIO.output(l_rev, 0)
 	GPIO.output(l_for, 1)

def stop(event):
 	GPIO.output(r_rev, 0)
 	GPIO.output(r_for, 0)
 	GPIO.output(l_rev, 0)
 	GPIO.output(l_for, 0)

root = Tk()
root.bind('<Up>', up_arrow)
root.bind('<Down>', down_arrow)
root.bind('<Left>', left_arrow)
root.bind('<Right>', right_arrow)
root.bind('<space> ', stop)
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()