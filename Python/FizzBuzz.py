"""
Classic FizzBuzz problem.
If number is a multiple of 3 & 5 print FizzBuzz.
If number is a multiple of 3, print Fizz.
if number is a multiple of 5, print Buzz.
Else print the number
"""

def main():
    number = int(input("Enter a number for the test: "))
    for i in range(1, number):
        if ( i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    main()
