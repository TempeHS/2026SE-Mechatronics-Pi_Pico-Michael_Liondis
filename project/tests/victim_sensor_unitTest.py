from victim_sensor import Victim_Sensor             # import victim sensor class
from PiicoDev_VEML6040 import PiicoDev_VEML6040     # import coloir sensor class
from PiicoDev_SSD1306 import *                      # import OLED screen class
from PiicoDev_Unified import sleep_ms               # import sleep in miliseconds
from time import sleep                              # import sleep 

# instatiate sensors and display
sensor = PiicoDev_VEML6040()
display = create_PiicoDev_SSD1306()

# instatiate victim sensor 
Victim_Sensor = Victim_Sensor(display, sensor, False)

print("testing victim sensor")
sleep(2)        
print("testing SenseVictim")
while True:
    print(Victim_Sensor.SenseVictim())     # prints continus loop of sensing the victim
    sleep(0.1)                             # sleeps for 0.1 seconds