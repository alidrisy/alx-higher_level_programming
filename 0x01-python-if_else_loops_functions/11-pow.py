#!/usr/bin/python3
def pow(a, b):
    x = a
    if a == 0:
        return 0
    elif a > 0:
        if b == 0:
            return 1
        elif b > 0:
            for i in range(1,b):
                x *= a
        else:
            while b != 1:
                x /= a
                b += 1
    else:
        x = abs(x)
        if b == 0:
            x = 1
        elif b > 0:
            for i in range(1,b):
                x *= a
            x = -(x)
        else:
            while b != 1:
                x /= a
                b += 1
            x = -(x)
    return x
