from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

colourSensor = PiicoDev_VEML6040()

display = create_PiicoDev_SSD1306()

class VictimSensor:
    def __init__(self, display, colourSensor, debug=True):
        self.__display = display
        self.__colourSensor = colourSensor
        self.__debug = debug

    def sense_victim(self):
        while True:
            data = self.__colourSensor.readHSV()
            hue = data['hue']

            label = colourSensor.classifyHue() # Read the sensor again, this time classify the colour
            print(str(label) + " Hue: " + str(hue))

            sleep_ms(1000)