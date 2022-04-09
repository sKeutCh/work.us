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

    def __eq__(self, other) -> bool:
        return self.top == other.top and self.bottom == other.bottom

    def reduce(self):
        p = math.gcd(self.top, self.bottom)
        self.top = self.top // p
        self.bottom = self.bottom // p
