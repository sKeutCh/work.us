import math


class Fraction:
    def __init__(self, nume=0, denom=1):
        self.top = nume
        self.bottom = denom

    def input(self):
        self.top = int(input("Введите числитель: "))
        self.bottom = int(input("Введите знаменатель: "))
        if self.bottom == 0:
            raise ValueError("Знаменатель не равен 0")

    def __str__(self):
        return str(self.top)+"/"+str(self.bottom)

    def reduce(self):
        p = math.gcd(self.top, self.bottom)
        return str(self.bottom / p)+'/'+str(self.bottom / p)


p = Fraction()
print(p)

b1 = Fraction()
print(b1)

b2 = Fraction(3, 4)
print(b2)

b3 = Fraction()
b3.input()
print(b3)