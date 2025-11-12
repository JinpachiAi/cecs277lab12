from plate import Plate


class SmallPlate(Plate):
    
    """
    A small plate with a fixed area and weight limit. 
    
    Attributes:
        Plate: The base Plate class.
    Returns:
        description (str): A description of the plate.
        area (int): The area of the plate in square inches(according to the table provided).
        weight (int): The weight limit of the plate in ounces(according to the table provided).
        count(int): The items on the plate is zero at the start.
    """
    
    def description(self):
        
        return f"Sturdy 10 inch paper plate"
    
    
    def area(self):
        
        return 78
    
    
    def weight(self):
        
        return 32
    
    def count(self):
        return 0