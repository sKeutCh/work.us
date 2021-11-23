def arifm(x):
    d = sum(x) / len(x)
    print("Средн. арифм.", d)
n = input()
b = []
while n != '':
    b.append(float(n))
    n = input()
arifm(b)