"""
Makes a password. Not the best, but makes something.
Might add validator.
"""

import string
import random

def password_maker(length):
    '''
    password maker
    '''
    if length >= 8:
        password_variables = ''.join((string.ascii_letters, string.digits, string.punctuation))
        password = ''.join(random.choice(password_variables) for i in range(length))
        #print(password)
        return password
    else:
        print("Password length too short. Try again")
        print("-"*45)
        main()


def main():

    print("-"*45)
    print("Enter the length you want your password to be.")
    print("Secure passwords are recommended to be 8 or more letters in legnth.\n")

    try:
        length = int(input("How many characters do you want in your password? "))
    except ValueError:
        print("You did not enter an integer.")
    else:
        password = password_maker(length)
        value = input("What's the password for? Blog, email, etc: ")

        storage = {}
        storage[value] = password

        for k, v in storage.items():
            print("{}: {}".format(k, v))




if __name__ == '__main__':
    main()
