
import abc
from plate import Plate

class PlateDecorator(Plate, abc.ABC):
        
        """
        Abstract decorator class. Inherits from the plate interface and initializes a plate. Uses methods from plate. 
        """
        def __init__(self, p):
                self._plate = p

        def description(self):
                return self._plate.description()

        def area(self):
                return self._plate.area()

        def weight(self):
                return self._plate.weight()

        def count(self):
                return self._plate.count()