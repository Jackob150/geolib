from utils.test_utils import get_point_from_input
from utils.test_utils import get_vector_from_input
from utils.test_utils import get_line_from_input
from utils.test_utils import get_float_from_input
from tests.point.cases import *

from src.geolib import *

import pytest


@pytest.mark.parametrize("input, result", distance_from_point_cases)
def test_distance_from_point(test_manager, input, result):
    status, logger = test_manager
    p = get_point_from_input(input, 0)
    q = get_point_from_input(input, 1)
    assert p.get_dist_from_point(q) == result
    assert q.get_dist_from_point(p) == result

@pytest.mark.parametrize("input, result", distance_from_line_cases)
def test_distance_from_line(test_manager, input, result):
    p = get_point_from_input(input, 0)
    l = get_line_from_input(input, 1)
    assert p.get_dist_from_line(l) == result

@pytest.mark.parametrize("input, result", move_by_vector_cases)
def test_move_by_vector(test_manager, input, result):
    p = get_point_from_input(input, 0)
    v = get_vector_from_input(input, 1)
    p.move_by_vector(v)
    assert p == get_point_from_input(result, 0)

@pytest.mark.parametrize("input, result", get_moved_by_vector_cases)
def test_get_moved_by_vector(test_manager, input, result):
    p = get_point_from_input(input, 0)
    v = get_vector_from_input(input, 1)
    assert p.get_moved_by_vector(v) == get_point_from_input(result, 0)

@pytest.mark.parametrize("input, result", rotate_around_origin_cases)
def test_rotate_around_origin(test_manager, input, result):
    p = get_point_from_input(input, 0)
    alpha = get_float_from_input(input, 1)
    p.rotate_around_origin(alpha)
    assert p == get_point_from_input(result, 0)

@pytest.mark.parametrize("input, result", get_rotated_around_origin_cases)
def test_get_rotated_around_origin(test_manager, input, result):
    p = get_point_from_input(input, 0)
    alpha = get_float_from_input(input, 1)
    assert p.get_rotated_around_origin(alpha) == get_point_from_input(result, 0)

@pytest.mark.parametrize("input, result", rotate_around_point_cases)
def test_rotate_around_point(test_manager, input, result):
    p = get_point_from_input(input, 0)
    q = get_point_from_input(input, 1)
    alpha = get_float_from_input(input, 2)
    p.rotate_around_point(q, alpha)
    assert p == get_point_from_input(result, 0)

@pytest.mark.parametrize("input, result", get_rotated_around_point_cases)
def test_get_rotated_around_point(test_manager, input, result):
    p = get_point_from_input(input, 0)
    q = get_point_from_input(input, 1)
    alpha = get_float_from_input(input, 2)
    assert p.get_rotated_around_point(q, alpha) == get_point_from_input(result, 0)