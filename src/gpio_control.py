#!/usr/bin/env python

import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import Int32 


def toggleGPIO(pin):
  pin = pin.data
  if pin in pins:
    GPIO.output(pin, int(GPIO.input(pin) == 0))
    rospy.loginfo("Changed pin {}".format(pin))
  else:
    rospy.loginfo("Changed pin {} and added to pins list".format(pin))
    GPIO.setup(pin, GPIO.OUT)
    pins.append(pin)
    GPIO.output(pin, 1)


if __name__ == "__main__":
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  pins = []
  rospy.init_node("gpio_control")
  rospy.Subscriber("gpio_control", Int32, toggleGPIO)
  rospy.loginfo("gpio_control loaded")
  
  rospy.spin()
  GPIO.cleanup()

