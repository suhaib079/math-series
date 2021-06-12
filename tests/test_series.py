from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series


def test_version():
    assert __version__ == '0.1.0'



# testing fibonacci

def test_fibonacci():
    expected =3
    actual = fibonacci(4)
    assert actual== expected

def test_fibonacci2():
    expected =8
    actual = fibonacci(6)
    assert actual== expected

def test_fibonacci3():
    expected =13
    actual = fibonacci(7)
    assert actual== expected


    # testing  locus 

def test_lucas():
    expected = 11
    actual = lucas(5)
    assert actual == expected

def test_lucas2():
    expected = 18
    actual = lucas(6)
    assert actual == expected

def test_lucas3():
    expected = 7
    actual = lucas(4)
    assert actual == expected




def test_sum_series():
    assert sum_series(2) == 1



