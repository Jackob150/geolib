import pytest

from src.geolib import *
from utils.test_utils import get_line_from_input, get_point_from_input, get_vector_from_input, get_float_from_input
from tests.line.cases import *
from src.exceptions import PointOutsideLine

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

@pytest.mark.parametrize("input, result", get_OX_intersection_cases)
def test_get_OX_intersection(test_manager, input, result):
    l = get_line_from_input(input, 0)
    assert l.get_OX_intersection() == result

@pytest.mark.parametrize("input, result", get_OY_intersection_cases)
def test_get_OY_intersection(test_manager, input, result):
    l = get_line_from_input(input, 0)
    assert l.get_OY_intersection() == result

@pytest.mark.parametrize("input, result", get_gradient_formula_cases)
def test_get_gradient_formula(test_manager, input, result):
    l = get_line_from_input(input, 0)
    assert l.get_gradient_formula() == result

@pytest.mark.parametrize("input, result", get_line_intersection_cases)
def test_get_line_intersection(test_manager, input, result):
    l = get_line_from_input(input, 0)
    m = get_line_from_input(input, 1)
    assert l.get_line_intersection(m) == get_point_from_input(result, 0)
    assert m.get_line_intersection(l) == get_point_from_input(result ,0)

@pytest.mark.parametrize("input, result", get_perp_line_cases)
def test_get_perp_line(test_manager, input, result):
    p = get_point_from_input(input, 1)
    l = get_line_from_input(input, 0)
    assert l.get_perp_line(p) == get_line_from_input(result, 0)

@pytest.mark.parametrize("input, result", get_parallel_line_cases)
def test_get_parallel_line(test_manager, input, result):
    p = get_point_from_input(input, 1)
    l = get_line_from_input(input, 0)
    assert l.get_parallel_line(p) == get_line_from_input(result, 0)

@pytest.mark.parametrize("input, result", get_dist_from_point_cases)
def test_get_dist_from_point(test_manager, input, result):
    p = get_point_from_input(input, 0)
    l = get_line_from_input(input, 1)
    assert abs(l.get_dist_from_point(p) - result) < epsilon

@pytest.mark.parametrize("input, result", get_dist_from_line_cases)
def test_get_dist_from_line(test_manager, input, result):
    l = get_line_from_input(input, 0)
    m = get_line_from_input(input, 1)
    assert (l.get_dist_from_line(m) - result) < epsilon
    assert (m.get_dist_from_line(m) - result) < epsilon

@pytest.mark.parametrize("input, result", rotate_by_angle_cases)
def test_rotate_by_angle(test_manager, input, result):
    _, logger = test_manager
    l = get_line_from_input(input, 0)
    p = get_point_from_input(input, 1)
    alpha = get_float_from_input(input, 2)
    try:
        l.rotate_by_angle(alpha, p)
    except PointOutsideLine as e:
        logger.info(e)
        assert l == get_line_from_input(input, 0)
    else:
        assert l == get_line_from_input(result, 0)
        l.rotate_by_angle(-alpha, p)
        assert l == get_line_from_input(input, 0)

@pytest.mark.parametrize("input, result", get_rotated_by_angle_cases)
def test_get_rotated_by_angle(test_manager, input, result):
    _, logger = test_manager
    l = get_line_from_input(input, 0)
    p = get_point_from_input(input, 1)
    alpha = get_float_from_input(input, 2)
    assert l.get_rotated_by_angle(alpha, p) == get_line_from_input(result, 0)
