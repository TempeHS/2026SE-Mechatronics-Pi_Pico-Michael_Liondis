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

        def idle_state(self): #     STOP state
            if self.__debug:
                print("System: IDLE state")
            self.state = "IDLE"
            self.__wheels.stop()

        def set_read_dist(self):
            if self.__debug:
                print("System: READ state")
            self.state = "READ"
            print(Lultra.distance_mm, Fultra.distance_mm)

        def move_forward(self):
            if self.__debug:
                print("System: FORWARDS state")
            self.state = "FORWARDS"
            self.__wheels.move_forward()

        def set_move_backwards_state(self):
            if self.__debug:
                print("System: BACKWARDS state")
            self.state = "BACKWARDS"
            self.__wheels.move_backward()

        def set_rotate_right_state(self):
            if self.__debug:
                print("System: RIGHT state")
            self.state = "RIGHT"
            self.__wheels.rotate_right()

        def set_rotate_left_state(self):
            if self.__debug:
                print("System: LEFT state")
            self.state = "LEFT"
            self.__wheels.rotate_left()

        def error_state(self):
            if self.__debug:
                print("System: ERROR state")
            self.state = "ERROR"
            self.__wheels.stop() 

        def update(self):
            time_now = time.now()
            if self.state == "IDLE":
                self.idle_state()
                if self.__last_state_change - time_now >= 5:
                    self.set_forwards_state()
            elif self.state == "READ":
                self.set_read_dist()
            elif self.state == "FORWARDS":
                self.set_move_forwards_state()
            elif self.state == "BACKWARDS":
                self.set_move_backwards_state()
            elif self.state == "RIGHT":
                self.set_rotate_right_state()
            elif self.state == "LEFT":
                self.set_rotate_left_state()
            else:
                self.error_state()