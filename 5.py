x = float(input())
y = float(input())
if x > 0 and y > 0:
    print('1 четверть')
elif x < 0 and y < 0:
    print('2 четверть')
elif x > 0 and y < 0:
    print('3 четверть')
else:
    print('на оси')