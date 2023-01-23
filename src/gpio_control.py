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
  GPIO.output(7, gui_data.gpio_pin_7)
  GPIO.output(11, gui_data.gpio_pin_11)
  GPIO.output(13, gui_data.gpio_pin_13)
  GPIO.output(15, gui_data.gpio_pin_15)
  GPIO.output(19, gui_data.gpio_pin_19)
# Main function
if __name__ == "__main__":
  GPIO.setmode(GPIO.BOARD)
  GPIO.setwarnings(False)
  
  # Initialize GPIOs in output mode
  GPIO.setup(7, GPIO.OUT)
  GPIO.output(7, 0)
  GPIO.setup(11, GPIO.OUT)
  GPIO.output(11, 0)
  GPIO.setup(13, GPIO.OUT)
  GPIO.output(13, 0)
  GPIO.setup(15, GPIO.OUT)
  GPIO.output(15, 0)
  GPIO.setup(19, GPIO.OUT)
  GPIO.output(19, 0)
  
  # Create ROS Node and Subscriber
  rospy.init_node("gpio_control")
  rospy.Subscriber("/control", controlData, toggleGPIO)
  
  #Stop the program from exiting
  rospy.spin()
  
  # Good practice to run this function when the program exits.
  GPIO.cleanup()

