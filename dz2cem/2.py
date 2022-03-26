from fraction import Fraction


class IrreducibleFraction(Fraction):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reduce()

    def input(self, *args, **kwargs):
        super().input(*args, **kwargs)
        self.reduce()


a = IrreducibleFraction()
a.input()
print(a)
