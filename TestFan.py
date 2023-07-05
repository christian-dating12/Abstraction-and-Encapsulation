from Fan_Class import Fan

class TestFan:
    def __init__(self):

# Pseudocode
# For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
        first_obj = Fan(Fan.FAST, 10, "yellow", True)
# Assign medium speed, radius 5, color blue, and turn it off for the second object. 
        second_obj = Fan(Fan.MEDIUM, 5, "blue", False)
# Display each object’s speed, radius, color, and on properties.

        input("\n\033[93mPress Any Key to Start...\033[0m\n")
        print("\033[90m=" *100)
        print("\033[93m ------------------------- WELCOME! ------------------------- \033[0m".center(105))
        print("\033[90m=" *100)

        # First obj 
        print("\033[93m  FAN #1  \033[0m".center(105))
        print("\033[90m=" *100)

        print ("\n\033[96mSPEED = ", first_obj.get_speed())
        print ("\033[96mRADIUS = ", first_obj.get_radius())
        print ("\033[96mCOLOR = ", first_obj.get_color())
        print ("\033[96mSTATUS = ", first_obj.status_on())

        print("\033[90m=" *100)
        print("\033[93m  FAN #2  \033[0m".center(105))
        print("\033[90m=" *100)
        
        # Second obj
        print ("\n\033[96mSPEED = ", second_obj.get_speed())
        print ("\033[96mRADIUS = ", second_obj.get_radius())
        print ("\033[96mCOLOR = ", second_obj.get_color())
        print ("\033[96mSTATUS = ", second_obj.status_on())

TestFan()