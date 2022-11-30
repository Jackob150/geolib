from src.geolib import *

def get_float_from_input(input: list, index: int):
    return float(input[index])

def get_point_from_input(input: list, index: int):
    if input[index]:
        return Point(input[index][0], input[index][1])
    return None

def get_vector_from_input(input: list, index: int):
    if input[index] is not None:
        return Vector(input[index][0], input[index][1])
    return None

def get_line_from_input(input: list, index: int):
    if input[index] is not None:
        return Line(input[index][0], input[index][1], input[index][2])
    return None
