from time import time                   # import time for tracking state changes
from PiicoDev_Unified import sleep_ms   # sleep function in miliseconds 
from PiicoDev_SSD1306 import *          # OLED display library

# create OLED display object
display = create_PiicoDev_SSD1306()

class Controller: 
    def __init__(self, wheels, Lultra, Fultra, colour_sensor, debug):
        # store the references to wheels, ultrsonic sensor, and colour sensor
        self.__wheels = wheels
        self.__Lultra = Lultra          # left ultrasonic
        self.__Fultra = Fultra          # front ultrasonic 
        self.__colour = colour_sensor   # victim/colour sensor
        self.state = "IDLE"             # initial state
        self.last_state_change = time()
        self.__debug = debug

        self.turn_delay = 0.5           # delay before switching out of turn

    def idle_state(self): #STOP state
        if self.__debug:
            print("System: IDLE state")
        self.state = "IDLE"
        self.__wheels.stop()                # stops wheels
        self.last_state_change = time()

    def set_move_forwards_state(self):
        if self.__debug:
            print("System: FORWARDS state")
        self.state = "FORWARDS"
        self.__wheels.move_forward()        # drives forward 
        self.last_state_change = time()

    def set_move_backwards_state(self):
        if self.__debug:
            print("System: BACKWARDS state")
        self.state = "BACKWARDS"
        self.__wheels.move_backward()       # drives backwards
        self.last_state_change = time()

    def set_rotate_right_state(self):
        if self.__debug:
            print("System: RIGHT state")
        self.state = "RIGHT"
        self.__wheels.rotate_right()        # turns right
        self.last_state_change = time()

    def set_rotate_left_state(self):
        if self.__debug:
            print("System: LEFT state")
        self.state = "LEFT"
        self.__wheels.rotate_left()         # turns left
        self.last_state_change = time()

    def error_state(self):
        if self.__debug:
            print("System: ERROR state")
        self.state = "ERROR"
        self.__wheels.stop()                # stop robot on an error
        self.last_state_change = time()

    def update(self):
        now = time()

        # wait for delay to be over before doing anything after turning or going bakcwards
        if self.state in ("LEFT", "RIGHT", "BACKWARDS"):
            if now - self.last_state_change < self.turn_delay:
                return # continues the turn
            else:
                self.__wheels.move_forward()    # resumes forward motion
        
        # victim sensing logic
        VictimStatus = self.__colour.SenseVictim()

        if VictimStatus == "green":
            self.idle_state()               # stops robot
            sleep_ms(4000)                  # idle for 4000 miliseconds
            self.__wheels.move_forward()    # moves forward
            sleep_ms(500)                   # small forward movement to make sure it doesnt sense the same victim/colour again
        if VictimStatus == "not green":
            display.show()                  # refresh the display
            display.fill(0)                 # clear the display
        
        # read distances from ultrasonic sensors
        front_dist = self.__Fultra.distance_mm
        left_dist = self.__Lultra.distance_mm

        wall_dist = 100     # distance to the wall that the ultras will read

        # Case 1: wall in fron AND on left --> turn right (so left ultra is facing wall)
        if front_dist < wall_dist and left_dist < wall_dist:
            self.idle_state()             
            sleep_ms(2000)              
            self.set_rotate_right_state()
            sleep_ms(1050)
            self.idle_state()
            sleep_ms(2000)
            self.last_state_change = now

        # Case 2: Wall in front --> turn right (so left ultra is facing wall)
        elif front_dist < wall_dist:
            self.idle_state()
            sleep_ms(2000)
            self.set_rotate_right_state()
            sleep_ms(1050)
            self.idle_state()
            sleep_ms(2000)
            self.last_state_change = now
        
        # Case 3: No wall on left AND no wall in front --> turn left 
        elif left_dist > wall_dist:
            # turn left 
            sleep_ms(500)
            self.idle_state()
            sleep_ms(2000)
            self.set_rotate_left_state()
            sleep_ms(1050)
            self.idle_state()
            sleep_ms(2000)
            self.set_move_forwards_state()
            sleep_ms(500)
            self.last_state_change = now
        
        # Case 4: Default --> moves forwards
        else:
            self.set_move_forwards_state()