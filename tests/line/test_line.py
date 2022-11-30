import pytest

from src.geolib import *
from utils.test_utils import get_line_from_input, get_point_from_input, get_vector_from_input
from tests.line.cases import *

@pytest.mark.parametrize("input, result", directional_line_cases)
def test_directional_line(test_manager, input, result):
    assert Line.directional_line(input[0], input[1]) == get_line_from_input(result, 0)

@pytest.mark.parametrize("input, result", two_points_line_cases)
def test_two_points_line(test_manager, input, result):
    p = get_point_from_input(input, 0)
    q = get_point_from_input(input, 1)
    assert Line.two_points_line(p, q) == get_line_from_input(result, 0)
    assert Line.two_points_line(q, p) == get_line_from_input(result, 0)

@pytest.mark.parametrize("input, result", vector_line_cases)
def test_vector_line(test_manager, input, result):
    p = get_point_from_input(input, 0)
    v = get_vector_from_input(input, 1)
    assert Line.vector_line(p, v) == get_line_from_input(result, 0)
    assert Line.vector_line(p, v.get_scaled_vector(-1)) == get_line_from_input(result, 0)

@pytest.mark.parametrize("input, result", is_point_in_line_cases)
def test_is_point_in_line(test_manager, input, result):
    p = get_point_from_input(input, 0)
    l = get_line_from_input(input, 1)
    assert l.is_point_in_line(p) == result

@pytest.mark.parametrize("input, result", get_direction_cases)
def test_get_direction(test_manager, input, result):
    l = get_line_from_input(input, 0)
    assert l.get_direction() == get_vector_from_input(result, 0)

@pytest.mark.parametrize("input, result", get_gradient_cases)
def test_get_gradient(test_manager, input, result):
    l = get_line_from_input(input, 0)
    assert l.get_gradient() == result