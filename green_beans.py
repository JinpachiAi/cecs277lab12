from plate_decorator import PlateDecorator

class Beans(PlateDecorator):
    def description(self):
        return super().description() + " + green beans"

    def area(self):
        return super().area() - 20

    def weight(self):
        return super().weight() - 3

    def count(self):
        return super().count() + 1