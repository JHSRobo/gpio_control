#!/usr/bin/env python3

# For whatever reason, this script messes with the PATH, so we have to run this little command.
# I have no idea why it works. Newbies, ignore this part.
import sys
import os
sys.path.remove(os.path.dirname(__file__))

from gpio_control.msg import controlData
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import Bool

# Yes, I know the following code is gross.
# It makes it super simple to train newbies on, and we will be training a lot of newbies on this package.
def toggleGPIO(gui_data):
  
  # Set GPIO output for each pin equal to the value passed from the subscriber
  GPIO.output(23, gui_data.gpio_pin_7)
  GPIO.output(24, gui_data.gpio_pin_11)
  GPIO.output(25, gui_data.gpio_pin_13)
  GPIO.output(5, gui_data.gpio_pin_15)
  GPIO.output(19, gui_data.gpio_pin_19)
  GPIO.output(16, gui_data.gpio_pin_16)
# Main function
if __name__ == "__main__":
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  
  # Initialize GPIOs in output mode
  GPIO.setup(23, GPIO.OUT)
  GPIO.output(23, 0)
  GPIO.setup(24, GPIO.OUT)
  GPIO.output(24, 0)
  GPIO.setup(25, GPIO.OUT)
  GPIO.output(25, 0)
  GPIO.setup(5, GPIO.OUT)
  GPIO.output(5, 0)
  GPIO.setup(19, GPIO.OUT)
  GPIO.output(19, 0)
  GPIO.setup(16, GPIO.OUT)
  GPIO.output(16, 0)
  
  # Create ROS Node and Subscriber
  rospy.init_node("gpio_control")
  rospy.Subscriber("/control", controlData, toggleGPIO)
  
  #Stop the program from exiting
  rospy.spin()
  
  # Good practice to run this function when the program exits.
  GPIO.cleanup()

