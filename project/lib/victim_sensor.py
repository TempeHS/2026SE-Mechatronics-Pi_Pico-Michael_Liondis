class VictimSensor:
    def __init__(self, colourSensor, debug):
        #self.__display = display
        self.__colour_Sensor = colourSensor
        self.__debug = debug

    def sense_victim(self):
        if self.__debug:
            print("sensing")
        data = self.__colour_Sensor.readHSV()

        hue = data['hue']
        if hue > 75 and hue < 85:
            return "green"
        else:
            return "not green"