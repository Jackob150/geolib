import math

from src.geolib import *
from utils.interface import load_from_user


def run_example():
    """
    Example finding lines tangent to the circle originating from the same point outside the circle.
    """
    print(
        "\nProvide the circle parameters and a point to find lines"
        " tangent to the circle originating from given point.\n"
    )
    # Load data
    x = load_from_user("X coordinate of the circle center: ", 0)
    y = load_from_user("Y coordinate of the circle center: ", 0)
    r = load_from_user("Radius of the circle: ", 1)
    x_p = load_from_user("X coordinate of the point: ", math.sqrt(2))
    y_p = load_from_user("Y coordinate of the point: ", 0)
    # Given point
    outside_point = Point(x_p, y_p)
    # Given circle
    circle = Circle(r, Point(x, y))
    # Calculating distance between point and circle center
    distance = outside_point.get_dist_from_point(circle.center)
    # Point has to be outside the circle
    if distance > circle.radius:
        # Calculating tha angle between central line and tangent lines
        alpha = math.asin(circle.radius / distance)
        # Central line
        line = Line.two_points_line(outside_point, circle.center)
        # Tangent lines
        final_line_1 = line.get_rotated_by_angle(alpha, outside_point)
        final_line_2 = line.get_rotated_by_angle(-alpha, outside_point)
        # Printing results
        print(final_line_1)
        print(final_line_2)
    else:
        print("Given point inside the circle!")


if __name__ == "__main__":
    run_example()
