from custom_interfaces.srv import Ledctrl
import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO
import time

LED1 = 19
LED2 = 26

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(Ledctrl, 'leds_control', self.leds_control_callback)

    def leds_control_callback(self, request, response):
        response.led1_status = request.led1
        response.led2_status = request.led2
        if request.led1 == 0:
            led1_req = "OFF"
            GPIO.output(LED1, False)
        elif request.led1 == 1:
            led1_req = "ON"
            GPIO.output(LED1, True)
        elif request.led1 == 2:
            led1_req = "Blink"
        else:
            led1_req = "Error, please enter range 0 to 2 only" 
       
        if request.led2 == 0:
            led2_req = "OFF"
            GPIO.output(LED2, False)
        elif request.led2 == 1:
            led2_req = "ON"
            GPIO.output(LED2, True) 
        elif request.led2 == 2:
            led2_req = "Blink"
        else:
            led2_req = "Error, please enter range 0 to 2 only"
 
        self.get_logger().info('\nIncoming request\n  LED 1: %s \n  LED 2: %s' % (led1_req, led2_req))

        return response


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)
    GPIO.output(LED1, False)
    GPIO.output(LED2, False)

    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
