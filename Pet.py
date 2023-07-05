from Pet_Class import Pet

# Pseudocode

input("\n\033[93mPress Any Key to Start...\033[0m\n")
print("\033[90m=" *100)
print("\033[93m ------------------------- WELCOME! ------------------------- \033[0m".center(105))
print("\033[90m=" *100)

# Prompt the user to enter the name, type, and age of his or her pet. 
# This data should be stored as the object’s attributes. 

pet = Pet (input("\n\033[92mEnter the name of your pet: "), input("\n\033[92mEnter the type of your pet: "), input("\n\033[92mEnter the age of your pet: "))

print("\033[90m=" *100)

# Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.
print("\n\n\033[95mPET'S NAME: ", pet.get_name(), "\n\n\033[95mPET'S TYPE: ", pet.get_animal_type(), "\n\n\033[95mPET'S AGE: ", pet.get_age())

print("\033[90m=" *100)
print("\033[90m=" *100)
