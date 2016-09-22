"""
User enters length, and width of the room, also the cost of the tile.
Then program calculates the cost of the tile.
"""

def CostOfTile(length, width, cost):

    total = cost*width*length
    print("total cost for the tile is ${:.2f}".format(total))

def main():

    length = int(input("Enter length of room: "))
    width = int(input("Enter width of width: "))
    cost = float(input("Enter cost per tile: "))

    CostOfTile(length, width, cost)

if __name__ == '__main__':
    main()
