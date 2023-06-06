#!/usr/bin/python3
for num in range(0, 10):
    for num1 in range(num+1, 10):
        if num == 8 and num1 == 9:
            break
        print("{}".format(num % 10), end="")
        print("{}".format(num1 % 10), end=", ")
print("89")
