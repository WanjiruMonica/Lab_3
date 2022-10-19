# A program that prints all characters with ASCII code 1 to 255 using a for loop

def main():
    for i in range(256):
        print(i, end=' = ')
        print(chr(i))  # will print corresponding characters for all values of i


main()
