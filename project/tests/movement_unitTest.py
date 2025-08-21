from machine import Pin, PWM    # import pin and pwm for servos
from servo import Servo         # import servo class
from movement import Movement   # import movement class
from time import sleep          # import sleep for smooth unit testing

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

#instatiate left and right servo 
servo_pwm_left = PWM(Pin(16))
servo_pwm_right = PWM(Pin(15))

# instatiate left servo
left_servo = Servo(pwm=servo_pwm_left, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

# instatiate right servo
right_servo = Servo(pwm=servo_pwm_right, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

# instatiate movement 
movement = Movement(right_servo, left_servo, False)
print(isinstance(movement, Movement)) # true

print("Forward in 2 seconds")
sleep(2)
movement.move_forward()             # move forward 
print("Backward in 2 seconds")
sleep(2)
movement.move_backward()            # move backward
print("Stopping in 2 seconds")
sleep(2)
movement.stop()                     # stops
print("Turning right in 2 seconds")
sleep(2)
movement.rotate_right()             # turns right
print("Turning left in 2 seconds")
sleep(2)
movement.rotate_left()              # turns left
print("Stopping in 2 seconds")
sleep(2)
movement.stop()                     # stops