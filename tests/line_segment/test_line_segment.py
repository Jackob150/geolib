import pytest

from src.geolib import *
from tests.line_segment.cases import *
from utils.test_utils import (get_line_from_input, get_line_segment_from_input,
                              get_point_from_input, get_vector_from_input)


@pytest.mark.parametrize("input, result", vector_line_segment_cases)
def test_vector_line_segment(test_manager, input, result):
    p = get_point_from_input(input, 0)
    v = get_vector_from_input(input, 1)
    assert LineSegment.vector_line_segment(p, v) == get_line_segment_from_input(result, 0)

@pytest.mark.parametrize("input, result", get_length_cases)
def test_get_length(test_manager, input, result):
    ls = get_line_segment_from_input(input, 0)
    assert ls.get_length() == result

@pytest.mark.parametrize("input, result", get_center_cases)
def test_get_center(test_manager, input, result):
    ls = get_line_segment_from_input(input, 0)
    assert ls.get_center() == get_point_from_input(result, 0)

@pytest.mark.parametrize("input, result", get_segment_line_cases)
def test_get_segment_line(test_manager, input, result):
    ls = get_line_segment_from_input(input, 0)
    assert ls.get_segment_line() == get_line_from_input(result, 0)

@pytest.mark.parametrize("input, result", get_bisection_cases)
def test_get_bisection(test_manager, input, result):
    ls = get_line_segment_from_input(input, 0)
    assert ls.get_bisection() == get_line_from_input(result, 0)