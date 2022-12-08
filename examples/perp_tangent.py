import math
import time

from src.geolib import *

def load_from_user(prompt="", default=0, cast=float):
    try:
        in_data = cast(input(prompt))
    except:
        in_data = default
    finally:
        return in_data

def run_example():
    """
    Example finding lines tangent to the circle and perpendicular to the given line.
    """
    # Load data
    x = load_from_user("X coordinate of the circle: ", -2)
    y = load_from_user("Y coordinate of the circle: ", -1)
    r = load_from_user("Radius of the circle: ", 2*math.sqrt(10))
    print("Provide line coefficients in a form >> Ax + By + C = 0 <<")
    A = load_from_user("A: ", 3)
    B = load_from_user("B: ", -1)
    C = load_from_user("C: ", 0)

    # Given center of the circle
    circle_center = Point(x, y)
    # Given cirle
    main_circle = Circle(r, circle_center)
    # Given line
    main_line = Line(A, B, C)

    # Find the line, perpendicular to the given one, containing circle center
    perp_aux_line = main_line.get_perp_line(circle_center)
    # Find a vector parallel to the main line (pointing toward the tangent points)
    dir_vector = main_line.get_direction().get_normalized()
    # Find tangent points by moving from the circle center, parallely to the main line, by distance equal to the radius
    # of the circle (in two directions)
    tangent_point1 = circle_center.get_moved_by_vector(dir_vector.get_scaled_vector(main_circle.radius))
    tangent_point2 = circle_center.get_moved_by_vector(dir_vector.get_scaled_vector(-main_circle.radius))
    # Find lines perpendicular to the main line (parallel to the auxiliary lines) containing the tangent points
    final_line1 = perp_aux_line.get_parallel_line(tangent_point1)
    final_line2 = perp_aux_line.get_parallel_line(tangent_point2)

    # Printing results
    print("--------------------")
    print(f"Given circle: {main_circle}")
    print(f"Given line: {main_line}")
    print("Find lines perpendicular to the given one and tangent to the circle.")
    print("--------------------")
    print("Creating objects...")
    time.sleep(2)
    print("Solving equations...")
    time.sleep(2)
    print("Substitution of numerical values...")
    time.sleep(2)
    print("--------------------")
    print("Answer:")
    print(f"First line: {final_line1}")
    print(f"Second line: {final_line2}")

if __name__ == "__main__":
    run_example()