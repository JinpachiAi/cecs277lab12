"""
    LAB 12: Decorators
    Lesley Burgueno Beas
    Douglas Sam
    November 10th, 2025
"""
import check_input
from plate import Plate
from small_plate import SmallPlate
from large_plate import LargePlate
from plate_decorator import PlateDecorator
from turkey import Turkey
from stuffing import Stuffing  
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie



def examine_plate(p):
    """
    Displays the plate's description. Checks and displays the plate's remaining area and weight limit.
    If the plate's weight and area limit is zero, displays a fail message and returns True.

    Args:
        p(): plate

    Returns:
        boolean: returns True if plate spilled.
    """
    print(p.description())
    remaining_area = p.area()
    remaining_weight = p.weight()

    # print(f"remaining area : {remaining_area}")
    # print(f"remaining weight : {remaining_weight}")

    if remaining_area <= 0:
        print("Your plate isn't big enough for this much food! Your food spills over the edge.")
        return True
        
    elif remaining_weight <= 0:
        print("Your plate can't hold this much weight! Your plate breaks and your food goes everywhere.")
        return True
    
    if 1 <= remaining_weight <= 6:
        w_hint = "bending"
    elif 7 <= remaining_weight <= 12:
        w_hint = "weak"
    elif remaining_weight >= 13:
        w_hint = "strong"
        
    if 1 <= remaining_area <= 20:
        a_hint = "tiny bit"
    elif 21 <= remaining_area <= 40:
        a_hint = "some"
    elif remaining_area >= 41:
        a_hint = "plenty"
        
    print(f"Sturdiness: {w_hint}\nSpace available: {a_hint}")      
        

def main():
    
    #Prints welcome message.
    print ("-Thanksgiving Dinner-")
    print ("Serve yourself as much food as you like from the buffet, but make sure that your plate will hold without spilling everywhere!")
    
    #Lets user choose between small or large plate and initializes the user_plate instance.
    user_choice = check_input.get_int_range("Choose a plate:\n1.Small Sturdy Plate\n2. Large Flimsy Plate\n", 1, 2)

    if user_choice == 1:
        
        user_plate = SmallPlate()
        
    else:
        
        user_plate = LargePlate()
    
    
    #Sets plate spilled to false and starts the game loop.
    spilled = False
    while True:
        
        #Prints the menu and takes user choice.
        print("1. Turkey")
        print("2. Stuffing")
        print("3. Potatoes")
        print("4. Green Beans")
        print("5. Pie")
        print("6. Quit")
        food_choice = check_input.get_int_range("\n", 0, 6)
        
        if food_choice == 6:
            break
        if food_choice == 1:
            choice = Turkey(user_plate)
        elif food_choice == 2:
            choice = Stuffing(user_plate)
        elif food_choice == 3:
            choice = Potatoes(user_plate)
        elif food_choice == 4:
            choice = GreenBeans(user_plate)
        elif food_choice == 5:
            choice = Pie(user_plate)
        
        #Sets user's plate with the food choice and examines the plate.
        user_plate = choice
        spilled = examine_plate(user_plate)

        #If the plate's weight and/or area limit is zero the game ends.
        if spilled:
            break
    
    #If user selects option 6 from the menu and the plate has not spilled, then it displays a final message.
    if not spilled:
        items = user_plate.count()
        weight = user_plate.weight()
        area = user_plate.area()
        print(f"Good job! You made it to the table with {items} items.")
        print(f"There was still {area} square inches left on your plate.\nYour plate could have held {weight} more ounces of food")
        print("Don't worry, you can always go back for more. Happy Thanksgiving!")

if __name__ == "__main__":
    main()