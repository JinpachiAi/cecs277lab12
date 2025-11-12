from plate_decorator import PlateDecorator

class GreenBeans(PlateDecorator):
    
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
            return super().description() + " with green beans"
        else:
            return super().description() + " and green beans"


    def area(self):
        return super().area() - 20

    def weight(self):
        return super().weight() - 3

    def count(self):
        return super().count() + 1