import sys

from custom_interfaces.srv import Ledctrl
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(Ledctrl, 'leds_control')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Ledctrl.Request()

    def send_request(self, a, b):
        self.req.led1 = a
        self.req.led2 = b
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    future = minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(minimal_client, future)
    response = future.result()

    if response.led1_status == 0:
        led1_stat = "OFF"
    elif response.led1_status == 1:
        led1_stat = "ON"
    elif response.led1_status == 2:
        led1_stat = "Blink"
    else:
        led1_stat = "Error, please enter range 0 to 2 only" 
        
    if response.led2_status == 0:
        led2_stat = "OFF"
    elif response.led2_status == 1:
        led2_stat = "ON"
    elif response.led2_status == 2:
        led2_stat = "Blink"
    else:
        led2_stat = "Error, please enter range 0 to 2 only"

    minimal_client.get_logger().info(
        '\nLED status: \n  LED 1: %s \n  LED 2: %s' %
        (led1_stat, led2_stat))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
