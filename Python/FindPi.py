"""
Find Pi to the Nth Digit.
Ask user to enter a number, and have the program go that many decimal places.
There is a limit.
"""

import math


def CalculatePi(precision):
    while precision > 40:
        main()
    else:
        print("%.*f" % (precision, math.pi))

def main():
    precision = int(input("Enter the number of digits for pi: "))
    CalculatePi(precision)

if __name__ == '__main__':
    main()
