from Fan_Class import Fan

class TestFan:
    def __init__(self):

# Pseudocode
# For the first object, assign the maximum speed, radius 10, color yellow, and turn it on.
        first_obj = Fan(Fan.FAST, 10, "yellow", True)
# Assign medium speed, radius 5, color blue, and turn it off for the second object. 
        second_obj = Fan(Fan.MEDIUM, 5, "blue", False)
# Display each object’s speed, radius, color, and on properties.
        # First obj 
        print ("\nFAN #1 SPEED = ", first_obj.get_speed())
        print ("FAN #1 RADIUS = ", first_obj.get_radius())
        print ("FAN #1 COLOR = ", first_obj.get_color())
        print ("FAN #1 STATUS = ", first_obj.status_on())

        print("=" *50)

        # Second obj
        print ("FAN #2 SPEED = ", second_obj.get_speed())
        print ("FAN #2 RADIUS = ", second_obj.get_radius())
        print ("FAN #2 COLOR = ", second_obj.get_color())
        print ("FAN #2 STATUS = ", second_obj.status_on())

TestFan()