from plate import Plate


class LargePlate(Plate):
    """
    A large plate with a fixed area and weight limit. 
    
    Attributes:
        Plate: The base Plate class.
    Returns:
        description (str): A description of the plate.
        area (int): The area of the plate in square inches(according to the table provided).
        weight (int): The weight limit of the plate in ounces(according to the table provided).
        count(int): returns the items on the plate. 
    """
    
    def description(self):
        
        return f'Flimsy 12 inch paper plate'
    
    
    def area(self):
        
        return 113
    
    def weight(self):
        
        return 24
    
    def count(self):
        return 0