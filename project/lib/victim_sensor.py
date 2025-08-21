from PiicoDev_SSD1306 import *          # import pico OLED display library
from PiicoDev_Unified import sleep_ms   # import sleep function in miliseconds

# create OLED display object
display = create_PiicoDev_SSD1306()

class Victim_Sensor:
    def __init__(self, display, colour_sensor, debug=False):
        # instantiation of colour sensor and OLED screen
        self.__colour_sensor = colour_sensor
        self.__debug = debug
        self.__display = display

    def SenseVictim(self):
        if self.__debug:
            print("sensing")    # debug output when sensing starts 
        
        # read hsv values from colour sensor
        data = self.__colour_sensor.readHSV()

        # extract hue value
        hue = data['hue']

        # check if hue is within the green range 
        if hue > 75 and hue < 85:
            display.text("Victim Sensed",1,20, 1)   # write message on display
            display.show()                          # update display 
            return "green"                          # return detection of colour
        else:
            display.fill(0)                         # clear display if no victim
            return "not green"                      # return no detection 