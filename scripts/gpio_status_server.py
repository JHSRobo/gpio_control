#!/usr/bin/env python 

from gpio_control.srv import gpio_status, gpio_statusResponse
import rospy
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pins = []

def handle_gpio_status(req):
  """this is the function that does the actual returning"""
  if req.gpioNum not in pins:
    pins.append(req.gpioNum)
    GPIO.setup(req.gpioNum, GPIO.OUT)
  return gpio_statusResponse(GPIO.input(req.gpioNum))

if __name__ == "__main__":
  rospy.init_node('gpio_status_server')
  s = rospy.Service('gpio_status_server', gpio_status, handle_gpio_status)
  rospy.loginfo("gpio_status_server.py: GPIO status server started")
  rospy.spin()
