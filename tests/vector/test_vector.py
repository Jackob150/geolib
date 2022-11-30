import pytest

from src.geolib import *
from src.constans import epsilon
from tests.vector.cases import *
from utils.test_utils import get_point_from_input, get_vector_from_input


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

@pytest.mark.parametrize("input, result", normalize_cases)
def test_normalize(test_manager, input, result):
    _, logger = test_manager
    v = get_vector_from_input(input, 0)
    try:
        v.normalize()
    except ZeroLengthVectorNormalized as e:
        logger.info(e)
    else:
        assert v == get_vector_from_input(result, 0)
        assert abs(v.get_length() - result[1]) < epsilon

@pytest.mark.parametrize("input, result", get_normalized_cases)
def test_get_normalized(test_manager, input, result):
    v = get_vector_from_input(input, 0)
    assert v.get_normalized() == get_vector_from_input(result, 0)
    if v.x or v.y:
        assert abs(v.get_normalized().get_length() - result[1]) < epsilon

@pytest.mark.parametrize("input, result", get_moved_point_cases)
def test_get_moved_point(test_manager, input, result):
    p = get_point_from_input(input, 0)
    v = get_vector_from_input(input, 1)
    assert v.get_moved_point(p) == get_point_from_input(result, 0)

@pytest.mark.parametrize("input, result", get_vector_sum_cases)
def test_get_vector_sum(test_manager, input, result):
    v = get_vector_from_input(input, 0)
    w = get_vector_from_input(input, 1)
    assert v.get_vector_sum(w) == get_vector_from_input(result, 0)

@pytest.mark.parametrize("input, result", add_vector_cases)
def test_add_vector(test_manager, input, result):
    v = get_vector_from_input(input, 0)
    w = get_vector_from_input(input, 1)
    v.add_vector(w)
    assert v == get_vector_from_input(result, 0)