#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#Set GPIO pins
LED_Orange = 26
LED_Red = 19

#set GPIO direction (IN / OUT)
GPIO.setup(LED_Orange, GPIO.OUT)
GPIO.setup(LED_Red, GPIO.OUT)

while True:
    GPIO.output(LED_Orange, True)
    GPIO.output(LED_Red, False)
    time.sleep(1)
    GPIO.output(LED_Orange, False)
    GPIO.output(LED_Red, True)
    time.sleep(1)
