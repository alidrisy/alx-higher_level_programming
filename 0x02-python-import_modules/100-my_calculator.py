#!/usr/bin/python3
if __name__ == "__main__":
     import sys
     from calculator_1 import add, sub, mul, div
     argv = (sys.argv)
     x = len(argv) - 1
     if x != 3:
         print("Usage: ./100-my_calculator.py <a> <operator> <b>")
         exit(1)
     elif argv[2] not in '+-*/':
         print("Unknown operator. Available operators: +, -, * and /")
         exit(1)
     else:
         a = int(argv[1])
         b = int(argv[3])
         n = argv[2]
         if n == '+':
             print("{:d} {:s} {:d} = {:d}".format(a, n, b, add(a, b)))
         elif n == '-':
             print("{:d} {:s} {:d} = {:d}".format(a, n, b, sub(a, b)))
         elif sys.argv[2] == '*':
             print("{:d} {:s} {:d} = {:d}".format(a, n, b, mul(a, b)))
         elif n == '/':
             print("{:d} {:s} {:d} = {:d}".format(a, n, b, div(a, b)))
