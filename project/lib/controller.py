from movement import Movement
from victim_sensor import Victim_Sensor
from PiicoDev_VL53L1X import PiicoDev_VL53L1X
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from servo import Servo
from machine import Pin, PWM
from time import sleep

range_front = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_left = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))

left_servo = Servo(pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

right_servo = Servo(pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

movement = Movement(right_servo, left_servo, False)

while True:
    print(range_front.distance_mm, range_left.distance_mm)
    sleep(0.1)
    if range_left.distance_mm <= 100:
        movement.move_forward()
    elif range_left.distance_mm >= 100:
        movement.stop()