from victim_sensor import VictimSensor
from PiicoDev_SSD1306 import *
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from time import sleep

colourSensor = PiicoDev_VEML6040()

display = create_PiicoDev_SSD1306()

VictimSensor = VictimSensor(display, colourSensor, True)

VictimSensor.sense_victim()