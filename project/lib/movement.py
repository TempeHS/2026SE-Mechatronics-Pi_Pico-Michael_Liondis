from machine import Pin, PWM
from servo import Servo
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

class Movement:
    def __init__(self, right_servo, left_servo, debug):
        self.__right_servo = right_servo
        self.__left_servo = left_servo
        self.__debug = debug

    def move_forward(self):
        ...

    def move_backwards(self):
        ...

    def rotate_right(self):
        ...

    def rotate_left(self):
        ...

    def stop(self):
        ... 