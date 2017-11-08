#!/usr/bin/env python
# import RPi.GPIO as GPIO
import video_dir
import car_dir
import motor
from socket import *
import datetime
from time import ctime, sleep  # Import necessary modules

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-',
            'xy_home']

busnum = 1  # Edit busnum to 0, if you uses Raspberry Pi 1 or 0

forward_time=12
turn_time = 14
turn_angle = 90
car_dir.setup(busnum=busnum)
motor.setup(busnum=busnum)  # Initialize the Raspberry Pi GPIO connected to the DC motor.
# vit_ideo_dir.home_x_y()
car_dir.home()
motor.setSpeed(int(50))
wait_time = 1
print "you have %s seconds to get the car to a safe place" %(wait_time)

sleep(wait_time)
motor.forward()
start = datetime.datetime.now()
while (datetime.datetime.now()-start).seconds < forward_time:
    car_dir.home()
    pass
motor.ctrl(0)

#while (datetime.datetime.now() -
#car_dir.turn_right()
#car_dir.turn_right()
#motor.forward()
print "pausing"
start= datetime.datetime.now()
#pause for 2 seconds
while (datetime.datetime.now()-start).seconds < 2:
    pass

print "turnign left"
car_dir.turn(turn_angle)

motor.forward()
start = datetime.datetime.now()

while (datetime.datetime.now()-start).seconds < turn_time:
    car_dir.turn(turn_angle)
    pass
motor.ctrl(0)
print "pausing again"
print "go home"
car_dir.home()
motor.forward()
start = datetime.datetime.now() 
while (datetime.datetime.now()-start).seconds < forward_time:
    pass
motor.ctrl(0)
