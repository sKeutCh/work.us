from dz3 import fun

def f(k):
    print('Элемент', ':', 'Частота')
    for x in set(k):
        y = k.count(x)
        print(x, ':', y)


k = fun()
print(f(k))
