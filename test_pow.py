from mypow import power
from math import pow

def test_pow():
    assert power(2, 3) == pow(2, 3)
    assert power(2, -3) == pow(2, -3)
    assert power(-2, 3) == pow(-2, 3)
    assert power(-2, -3) == pow(-2, -3)
    assert power(2, 0) == 1
