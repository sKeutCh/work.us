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
        return f"{self.top}/{self.bottom}"
    

b1 = Fraction()
print(b1)

b2 = Fraction(3, 4)
print(b2)

b3 = Fraction()
b3.input()
print(b3)



