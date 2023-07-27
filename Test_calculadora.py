from calculadora import *
import pytest

@pytest.mark.parametrize("a, b, res",[
    (2,4,6),
    (-4,6,2),
    (-5,-1,-6),
])
def test_suma(a, b, res):
    assert suma(a, b) == res

@pytest.mark.parametrize("a, b, res",[
    (2,4,-2),
    (-4,6,-10),
    (-5,-1,-4),
])
def test_resta(a, b, res):
    assert resta(a, b) == res