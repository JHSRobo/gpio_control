#!/usr/bin/env python3

import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import Bool
from gpio_control.msg import controlData

# Yes, I know the following code is gross.
# It makes it super simple to train newbies on, and we will be training a lot of newbies on this package.
def toggleGPIO(gui_data):
  
  # Set GPIO output for each pin equal to the value passed from the subscriber
  GPIO.output(3, gui_data.gpio_pin_3)
  GPIO.output(5, gui_data.gpio_pin_5)
  GPIO.output(7, gui_data.gpio_pin_7)
  GPIO.output(11, gui_data.gpio_pin_11)
  GPIO.output(13, gui_data.gpio_pin_13)

# Main function
if __name__ == "__main__":
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  
  # Initialize GPIOs in output mode
  GPIO.setup(3, GPIO.OUT)
  GPIO.output(3, 0)
  GPIO.setup(5, GPIO.OUT)
  GPIO.output(5, 0)
  GPIO.setup(7, GPIO.OUT)
  GPIO.output(7, 0)
  GPIO.setup(11, GPIO.OUT)
  GPIO.output(11, 0)
  GPIO.setup(13, GPIO.OUT)
  GPIO.output(13, 0)
  
  # Create ROS Node and Subscriber
  rospy.init_node("gpio_control")
  rospy.Subscriber("/control", Bool, toggleGPIO)
  
  #Stop the program from exiting
  rospy.spin()
  
  # Good practice to run this function when the program exits.
  GPIO.cleanup()

