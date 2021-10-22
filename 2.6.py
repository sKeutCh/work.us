a = []
b = input()
k = int(input())
for i in b:
    if i.isdigit():
        a.append(i)
print(a[k - 1])