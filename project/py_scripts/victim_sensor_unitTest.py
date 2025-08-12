from victim_sensor import VictimSensor
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from time import sleep

colourSensor = PiicoDev_VEML6040()

victim_sensor = VictimSensor(colourSensor, False)

while True:
    print(victim_sensor.sense_victim())
    sleep(0.1)