from src.geolib import Point
from src.geolib import Line
from src.geolib import Vector

import pytest

distance_from_point_cases = [([0,0,0,1], 1),
                             ([0,0,0,-1], 1),
                             ([0,0,1,0], 1),
                             ([1,-1,-5,-9], 10),
                             ([10,-10,10,-10], 0)]

distance_from_line_cases = [([0,0,0,1,0],0),
                            ([0,0,1,0,0],0),
                            ([0,0,1,1,0],0),
                            ([0,0,0,1,1],1),
                            ([0,0,0,1,-1],1),
                            ([0,0,0,-1,1],1),
                            ([0,0,1,0,1],1),
                            ([0,0,-1,0,1],1),
                            ([1,1,1,-1,0],0),
                            ([-3,4,3,-4,0],5),]

move_by_vector_cases = [([0,0,0,0],[0,0]),
                        ([0,0,1,0],[1,0]),
                        ([0,0,0,1],[0,1]),
                        ([0,0,1,1],[1,1]),
                        ([0,0,-1,-1],[-1,-1]),
                        ([1,-1,-1,1],[0,0]),]

@pytest.mark.parametrize("input, result", distance_from_point_cases)
def test_distance_from_point(input, result):
    p = Point(input[0], input[1])
    q = Point(input[2], input[3])
    assert p.get_dist_from_point(q) == result
    assert q.get_dist_from_point(p) == result

@pytest.mark.parametrize("input, result", distance_from_line_cases)
def test_distance_from_line(input, result):
    p = Point(input[0], input[1])
    l = Line(input[2], input[3], input[4])
    assert p.get_dist_from_line(l) == result

@pytest.mark.parametrize("input, result", move_by_vector_cases)
def test_move_by_vector(input, result):
    p = Point(input[0], input[1])
    v = Vector(input[2], input[3])
    p.move_by_vector(v)
    assert p.x == result[0]
    assert p.y == result[1]