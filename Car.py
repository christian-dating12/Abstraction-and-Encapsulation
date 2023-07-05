from Car_Class import Car

car_obj = Car (2023, "Ford")
# Pseudocode

# Call the accelerate method five times. 
# After each call to the accelerate method, get the current speed of the car and display it.
for i in range(1, 6):
    car_obj.acc()
    print("CURRENT SPEED: ", car_obj.get_speed())
# Then call the brake method five times. 
# After each call to the brake method, get the current speed of the car and display it.
for i in range(1, 6):
    car_obj.brake()
    print("CURRENT SPEED: ", car_obj.get_speed())