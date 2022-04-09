from app.fraction import Fraction


def test_reduce():
    a = Fraction(5, 10)
    a.reduce()
    assert a.top == 1
    assert a.bottom == 2

def test_str():
    a = Fraction(5, 10)
    assert str(a) == "5/10"

def test_input(mocker):
    mocker.patch("builtins.input", side_effect=['1', '2'])
    a = Fraction()
    a.input()
    assert a.top == 1
    assert a.bottom == 2

def test_eq():
    a = Fraction(5, 10)
    b = Fraction(5, 10)
    assert a == b

def test_not_eq():
    a = Fraction(5, 10)
    b = Fraction(7, 8)
    assert a != b