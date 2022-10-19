# A program that asks for user input strictly from 0 to 9
# Prints the number in words

def main():
    number = int(input("Enter a number in the range 0-9: ")) #asks for input
    if number == 0:
        print("zero")

    elif number == 1:
        print("one")

    elif number == 2:
        print("Two")

    elif number == 3:
        print("three")

    elif number == 4:
        print("four")

    elif  number == 5:
        print("five")

    elif number == 6:
        print("six")

    elif number == 7:
        print("seven")

    elif number == 8:
        print("eight")

    elif number == 9:
        print("nine")

    else:                   # Ensures the user inputs a number in specified range
        print("Number out of range!")

main()
