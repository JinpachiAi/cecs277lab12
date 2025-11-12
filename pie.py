from plate_decorator import PlateDecorator

class Pie(PlateDecorator):
    
    """
    Attributes:
        PlateDecorator: The base plate decorator class to extend.
    Returns:
        description(str): description of the plate plus the food item.
        area(int): modified area of the plate
        weight(int): modified weight of the plate
        count(int): modified count of food items on the plate
    """
    
    def description(self):
        if super().count() == 0:
            return super().description() + " with pie"
        else:
            return super().description() + " and pie"

    def area(self):
        return super().area() - 19

    def weight(self):
        return super().weight() - 8

    def count(self):
        return super().count() + 1