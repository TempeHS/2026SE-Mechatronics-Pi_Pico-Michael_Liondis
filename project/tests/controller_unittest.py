from controller import Controller                       # import the controller class
from movement import Movement                           # import the movement class
from victim_sensor import Victim_Sensor                 # import the victim sensor class
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic     # import the ultrasonic class
from PiicoDev_VEML6040 import PiicoDev_VEML6040         # import colour senor class
from PiicoDev_SSD1306 import *                          # import OLED screen class
from servo import Servo                                 # import servo class
from machine import Pin, PWM                            # import pin and pwm for servo 
from time import sleep                                  # import sleep for organised unt testing

# Instantiating the left and front ultrasonics 
range_front = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_left = PiicoDev_Ultrasonic(id=[1, 0, 0, 0])

# creating sensor and display objects 
sensor = PiicoDev_VEML6040()
display = create_PiicoDev_SSD1306()

# instatiating victim sensor class 
Victim_Sensor = Victim_Sensor(display, sensor, False)

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))

# instatiate left servo 
left_servo = Servo(pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

# instatiate right servo 
right_servo = Servo(pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

# instataite movement object
movement = Movement(right_servo, left_servo, False)

# instatiate system object for the controller 
system = Controller(movement, range_left, range_front, Victim_Sensor, True)

print("testing system")
sleep(2)
print("set forwards state")
system.set_move_forwards_state()        # moves forwards
sleep(2)
print("set idle state")
system.idle_state()                     # stops 
sleep(2)
print("set backwards state")
system.set_move_backwards_state()       # moves backwards
sleep(2)
print("set lturn state")
system.set_rotate_left_state()          # turns left
sleep(2)
print("set rturn state")
system.set_rotate_right_state()         # turns right
sleep(2)
print("set error state")
system.error_state()                    # runs error state
sleep(2)
print("set update state")
system.update()                         # runs update state
sleep(2)