from utils.test_utils import get_point_from_input
from utils.test_utils import get_vector_from_input
from utils.test_utils import get_float_from_input
from tests.vector.cases import *

from src.geolib import *

import pytest


@pytest.mark.parametrize("input, result", two_points_vector_cases)
def test_two_points_vector(test_manager, input, result):
    p = get_point_from_input(input, 0)
    q = get_point_from_input(input, 1)
    v = Vector.two_points_vector(p, q)
    assert v == get_vector_from_input(result, 0)

@pytest.mark.parametrize("input, result", line_segment_vector_cases)
def test_line_segment_vector(test_manager, input, result):
    p = get_point_from_input(input, 0)
    q = get_point_from_input(input, 1)
    ls = LineSegment(p, q)
    v = Vector.line_segment_vector(ls)
    assert v == get_vector_from_input(result, 0)

@pytest.mark.parametrize("input, result", get_length_cases)
def test_get_length(test_manager, input, result):
    v = get_vector_from_input(input, 0)
    assert v.get_length() == result