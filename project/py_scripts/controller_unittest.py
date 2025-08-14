from controller import Controller  
from movement import Movement
from victim_sensor import Victim_Sensor
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *
from servo import Servo
from machine import Pin, PWM
from time import sleep

range_front = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_left = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

sensor = PiicoDev_VEML6040()
display = create_PiicoDev_SSD1306()

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))

left_servo = Servo(pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

right_servo = Servo(pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

movement = Movement(right_servo, left_servo, False)

system = Controller(movement, range_left, range_front, sensor, True)

while True: 
    print("testing system")
    sleep(2)
    print("testing forwards state")
    system.move_forward()
    sleep(2)
    print("testing idle state")
    system.idle_state()
    sleep(2)
    print("testing backwards state")
    system.set_move_backwards_state()
    sleep(2)
    print("testing lturn state")
    system.set_rotate_left_state()
    sleep(2)
    print("testing rturn state")
    system.set_rotate_right_state()
    sleep(2)
    system.set_idle_state()







# while True:
#     print(range_front.distance_mm, range_left.distance_mm)
#     sleep(0.1)
#     if range_left.distance_mm <= 100:
#         movement.move_forward()
#     elif range_left.distance_mm >= 100:
#         movement.stop()