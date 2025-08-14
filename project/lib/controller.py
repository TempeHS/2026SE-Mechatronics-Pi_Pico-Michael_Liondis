from time import sleep, time

class Controller: 
    def __init__(self, wheels, Lultra, Fultra, colour_sensor, debug):
        self.__wheels = wheels
        self.__Lultra = Lultra
        self.__Fultra = Fultra
        self.__colour = colour_sensor
        self.state = "IDLE"
        self.last_state_change = time()
        self.__debug = debug

        self.turn_delay = 0.5

        def idle_state(self): #     STOP state
            if self.__debug:
                print("System: IDLE state")
            self.state = "IDLE"
            self.__wheels.stop()
            self.last_state_change = time()

        def set_move_forwards_state(self):
            if self.__debug:
                print("System: FORWARDS state")
            self.state = "FORWARDS"
            self.__wheels.move_forward()
            self.last_state_change = time()

        def set_move_backwards_state(self):
            if self.__debug:
                print("System: BACKWARDS state")
            self.state = "BACKWARDS"
            self.__wheels.move_backward()
            self.last_state_change = time()

        def set_rotate_right_state(self):
            if self.__debug:
                print("System: RIGHT state")
            self.state = "RIGHT"
            self.__wheels.rotate_right()
            self.last_state_change = time()

        def set_rotate_left_state(self):
            if self.__debug:
                print("System: LEFT state")
            self.state = "LEFT"
            self.__wheels.rotate_left()
            self.last_state_change = time()

        def error_state(self):
            if self.__debug:
                print("System: ERROR state")
            self.state = "ERROR"
            self.__wheels.stop() 
            self.last_state_change = time()

        def update(self):
            now = time()
 
            # wait for delay to be over before anything after move forwards
            if self.state in ("LEFT", "RIGHT", "BACKWARDS"):
                if now - self.last_state_change < self.turn_delay:
                    return # continues the turn
                else: 
                    self.move_forward()
                    return 
            
            # when senses victim, stops for 5 seconds then continues
            VictimStatus = self.__colour.SenseVictim()
            if VictimStatus == "green":
                self.idle_state()
                sleep(5)
                self.move_forward()
                return
             
            front_dist = self.__Fultra.distance_mm
            left_dist = self.__Lultra.distance_mm

            wall_dist = 150 

            # wall to the left and wall to the right 
            if front_dist < wall_dist and left_dist < wall_dist
                # turn right
                self.set_rotate_right_state()

            # wall in front    
            elif front_dist < wall_dist:
                #turn right so ultra is facing wall
                self.set_rotate_right_state()
            
            elif left_dist > wall_dist:
                self.set_rotate_left_state()
            
            else:
                self.set_move_forwards_state()