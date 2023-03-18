# gpio_control
ROS gpio_control package

Toggles GPIO pins on and off based on the pin number that is sent to the topic /gpio_control

gpio_reader.py publishes the statuses of all of the GPIO pins we are using.
Those pins are GPIO numbers 4, 5, 6, 17, 22, 23, 24, 27.

This currently does not have a use, but it may be used for electromagnets or whatever in the future.
