import rclpy
from rclpy.node import Node

class GPIOController(Node):
    def __init__(self):
        super().__init__('gpio_control')

        # Quick reference for logging
        self.log = self.get_logger()

        self.gpio_nums = [ 4, 5, 6, 17, 22, 23, 24, 27 ]
        self.gpio_status = { 4: False, 5: False, 6: False, 17: False, 
                       22: False, 23: False, 24: False, 27: False }

        # Define Parameters
        for i in self.gpio_nums:
            self.declare_parameter(f"gpio{i}", False)

        # Timer, to always check for parameter updates
        self.timer = self.create_timer(0.25, self.timer_callback)

    def timer_callback(self):
        for i in self.gpio_nums:
            parameter_val = self.get_parameter(f"gpio{i}").value
            if self.gpio_status[i] is not parameter_val:
                self.gpio_status[i] = parameter_val
                if parameter_val: 
                    self.log.info(f"Turned pin {i} on")
                else: 
                    self.log.info(f"Turned pin {i} off")
                self.log.info("This code is just a GPIO simulation.")

def main():
    rclpy.init()

    gpio = GPIOController()

    # Runs the program until shutdown is recieved
    rclpy.spin(gpio)

    # On shutdown, kill node
    gpio.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

