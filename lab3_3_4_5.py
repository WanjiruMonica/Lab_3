# A program to test different manipulation techniques of a string 

def main():
    str = "This sentence has 27 chars."

    for c in str:
        print("({})".format(c),end="") # prints each letter individually inside a parenthesis
    print()
    
    for i in range(len(str)): # will print the whole string
        print(str[i],end='')
    print()
    
    for j in range(7):  # will print the first 6 indices
        print(str[j],end='')
    print()

    for k in range(1,7):  # will print from index 1 till index 6
        print(str[k],end='')
    print()

    for l in reversed(range(27)): #will reverse order of letterrs. NB:using range(26,1,-1) will reverse still, but will exclude Th
        print(str[l],end='')
    print()
        

main()
