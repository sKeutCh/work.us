def season(n):
    if 1 <= n <= 2 or n == 12:
        return ('winter')
    elif 3 <= n <= 5:
        return ('spring')
    elif 6 <= n <= 8:
        return ('summer')
    elif 9 <= n <= 11:
        return ('autumn')
    else:
        return ('no season')


n = int(input())
print(season(n))
