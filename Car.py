from Car_Class import Car

car_obj = Car (2023, "Ford")
# Pseudocode

input("\n\033[93mPress Any Key to Start...\033[0m\n")
print("\033[90m=" *100)
print("\033[93m ------------------------- WELCOME! ------------------------- \033[0m".center(105))
print("\033[90m=" *100)

# Call the accelerate method five times. 
# After each call to the accelerate method, get the current speed of the car and display it.

print("\033[93m ACCELERATE \033[0m".center(105))
print("\033[90m=" *100)

for i in range(1, 6):
    car_obj.acc()
    print("\033[97mCURRENT SPEED: ", car_obj.get_speed())
# Then call the brake method five times. 
# After each call to the brake method, get the current speed of the car and display it.
print("\033[90m=" *100)
print("\033[93m BRAKE  \033[0m".center(105))
print("\033[90m=" *100)
for i in range(1, 6):
    car_obj.brake()

    print("\033[97mCURRENT SPEED: ", car_obj.get_speed())