from large_plate import LargePlate
from small_plate import SmallPlate
from turkey import Turkey

def main():
    p = SmallPlate()
    p = Turkey(p)
    print(p.description())
    print(p.area())
    print(p.weight())

if __name__ == "__main__":
    main()