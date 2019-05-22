import pytest
from convrate import calc
from numpy import array

def test_witherr():
    err = [1e-2, 1e-4, 1e-8, 1e-16]
    r,C = calc.witherr(err)
    assert pytest.approx(r) == 2.0
    assert pytest.approx(C) == 1.0

def test_withsol():
    L = 1
    sol = array([1,1.1,1.11,1.1101,1.11010001])
    r,C = calc.withsol(sol)
    assert pytest.approx(r,0.1) == 2.0
    assert pytest.approx(C,0.1) == 1.0

def test_withsol2():
    L = 1
    sol = array([1e-1, 1e-2, 1e-4, 1e-8]) + L
    r,C = calc.withsol(sol, L)
    assert pytest.approx(r) == 2.0
    assert pytest.approx(C) == 1.0
