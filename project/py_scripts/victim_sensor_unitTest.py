from victim_sensor import VictimSensor
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from PiicoDev_Unified import sleep_ms
from PiicoDev_SSD1306 import create_PiicoDev_SSD1306

colourSensor = PiicoDev_VEML6040()
display = create_PiicoDev_SSD1306()

victimsensor = VictimSensor(display, colourSensor, debug=True)

print('debug')
while True:
    victimsensor.sense_victim()
    sleep_ms(1000)