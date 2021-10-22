n = input()
k = n.count("(")
c = n.count(")")
if k > c:
    print("не хватает", k - c, "закрывающей скобки")
elif k < c:
    print("не хватает", k - c, "открывающей скобки")
else:
    print("все хорошо")