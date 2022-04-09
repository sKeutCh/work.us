from app.irreducible import IrreducibleFraction


def test_input(mocker):
    mocker.patch("builtins.input", side_effect=['2', '4'])
    a = IrreducibleFraction()
    a.input()
    assert a == IrreducibleFraction(1, 2)

def test_init():
    a = IrreducibleFraction(2, 4)
    assert a == IrreducibleFraction(1, 2)

