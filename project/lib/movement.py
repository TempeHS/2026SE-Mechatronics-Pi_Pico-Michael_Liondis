from machine import Pin, PWM       # import classes to control pin and pwm
from servo import Servo            # import servo class to control servo motors

#servo configuration values
freq = 50               # frequency in hz for pwm values
min_us = 500            # minimum pulse width 
max_us = 2500           # maximum pulse width
dead_zone_us = 1500     # neatural pulse width (stop)

# configure pwm for left and right servos for specific pins 
servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))

# create servo object for left servo 
left_servo = Servo(pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

# create servo object for right servo 
right_servo = Servo(pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

class Movement:
    def __init__(self, right_servo, left_servo, debug=True):
        # Instantiation of right and left servo motors
        self.__right_servo = right_servo
        self.__left_servo = left_servo
        self.__debug = debug

    def move_forward(self):
        if self.__debug:
            print("Moving Forward")
        # right & left servo turn forward
        self.__right_servo.set_duty(1000)
        self.__left_servo.set_duty(2000)

    def move_backward(self):
        if self.__debug:
            print("Moving Backwards")
        # right & left servo turn backward
        self.__right_servo.set_duty(2000)
        self.__left_servo.set_duty(1000)

    def rotate_right(self):
        if self.__debug:
            print("Turning Right")
        # right servo stops, left servo moves forward
        self.__right_servo.set_duty(1500)
        self.__left_servo.set_duty(2000)

    def rotate_left(self):
        if self.__debug:
            print("Turning Left")
        # right servo moves forward, left servo stops
        self.__right_servo.set_duty(1000)
        self.__left_servo.set_duty(1500)

    def stop(self):
        if self.__debug:
            print("Stop")
        # right & left servo stop
        self.__right_servo.stop()
        self.__left_servo.stop()