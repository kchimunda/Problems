"""
Find e to the Nth Digit.
Ask user to enter a number, and have the program go that many decimal places.
There is a limit. Similar to the FindPi.py file.
"""

import math


def CalculateE(precision):
    while precision > 40:
        main()
    else:
        print("%.*f" % (precision, math.e))

def main():
    precision = int(input("Enter the number of digits for e: "))
    CalculateE(precision)

if __name__ == '__main__':
    main()
