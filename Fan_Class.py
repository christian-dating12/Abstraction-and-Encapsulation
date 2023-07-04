class Fan:
    
# Pseudocode
# Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
    SLOW = 1
    MEDIUM = 2
    FAST = 3
# A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    # get fan speed
    def get_speed(self):
        if self.__speed == 1:
            self.__speed == "SLOW"
        elif self.__speed == 2:
            self.__speed == "MEDIUM"
        elif self.__speed == 3:
            self.__speed == "FAST"

# A private int data field named speed that specifies the speed of the fan.
    def set_speed(self, speed):
        self.__speed = speed
        
# A private bool data field named on that specifies whether the fan is on (the default is False).
    def status_on(self):
        return self.__on
    
    def set_on(self, on):
        self.__on == on
# A private float data field named radius that specifies the radius of the fan.
# A private string data field named color that specifies the color of the fan.
# The accessor(getters) and mutator(setters) methods for all four data fields.
