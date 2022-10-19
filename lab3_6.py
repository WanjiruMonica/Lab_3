def main():
    for i in range(20): 
        print("X" * i) # prints x from 1 to 19, each count on a different line

    for i in range(20):
        print("X" * (2 * i))

    for i in range(20):
        print("X"*i + "O"*i)

    for i in range(20):
        print("X"*i + "O"*(20-i))


main()
