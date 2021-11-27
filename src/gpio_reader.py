#!/usr/bin/env python

import RPi.GPIO as GPIO
import rospy
import time
print("bruh")
from gpio_control.msg import Reader 

print("Imported")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

rospy.init_node("gpio_reader")
print("Init node")
pub = rospy.Publisher('rov/gpio_readout', Reader, queue_size=10)

while not rospy.is_shutdown():
  output = [GPIO.input(4),
            GPIO.input(5),
            GPIO.input(6),
            GPIO.input(17),
            GPIO.input(22),
            GPIO.input(23),
            GPIO.input(24),
            GPIO.input(27) ]
  print(output)
  pub.publish(output)
  time.sleep(0.1)

GPIO.cleanup()
