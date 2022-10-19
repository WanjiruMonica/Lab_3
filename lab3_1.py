# A program that tests different uses of index and slicing

def main():
    name = "My name is Monica Wanjiru"
    print(name[0]) # prints first letter of sring
    print(name[24]) # prints last letter of string
    print(name[-25]) # prints first letter of string
    print(name[-1]) #prints last letter of string
    print(name[:2],end='') #This is slicing. Prints first word of string. Also will print next line of code on the same line without space
    print(name[18:25]) #This is also slicing. Prints last word of the string


main()
    

