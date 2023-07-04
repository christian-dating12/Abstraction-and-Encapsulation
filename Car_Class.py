class Car:
    
    def __init__(self, year_model = 2020, make = "Porsche", speed = 0 ):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

# Pseudocode
# The accelerate method should add 5 to the speed data attribute each time it is called.
    def acc(self):
        self.__speed += 5
# The brake method should subtract 5 from the speed data attribute each time it is called.
    def brake(self):
        self.__speed -= 5
# The get_speed method should return the current speed.
    def get_speed(self):
        return self.__speed