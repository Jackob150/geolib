from src.geolib import *
from utils.angles import *

def main():
    p = Point(0,0)
    q = Point(0,2)
    r = Point(3,0)
    b = Point(1,1)
    tr = Triangle(p,q,r)
    print(tr.get_length())
    print(tr.get_area())
    print(tr.get_center())
    print(tr.get_barycentric_coords(b))

if __name__ == "__main__":
    main()
