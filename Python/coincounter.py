"""
Asks user for what coin(s) they have and how much they weigh.
Once the coin is picked and weight entered in, program calculates how many
coin rolls they need. Coin rolls are the papers that hold a bunch of coins
together.
"""


def penny():
    pennyweight = 1.523
    print("Welcome to the Penny counter.\nHow much do they weigh?")
    weight = float(input("> "))

    total = int(weight/pennyweight)
    coinroll = int(total/14)

    print("You have a total of {} pennies.".format(total))
    print("Each penny-coin-roll holds 14 pennies, so you need ~{} rolls".format(coinroll))

    response = input("Want to add more coins? y/n")

    if response == 'y'.lower():
        return True
    else:
        return False

def nickel():
    pass
def dime():
    pass
def quarter():
    pass

def main():
    print("Welcome to the coin counter.")
    print("Tell me what coin(s) you have, and how much they weigh together.")
    print("You can only tell me the total of one coin at a time.\n")

    while True:
        answer = int(input("What coin do you have?\n1: penny\n2: nickel\n3: dime\n4: quarter\n>: "))

        if answer == 1:
            penny()
        elif answer == 2:
            nickel()
        elif answer == 3:
            dime()
        elif answer == 4:
            quarter()
        else:
            print("invalid input.")


if __name__ == '__main__':
    main()


# class Coin(object):
#
#     def __init__(self)
