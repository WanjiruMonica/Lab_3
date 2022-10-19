# A program that tests different indices and slicing

def main():
    str = "This sentence has 27 chars."
    print("1)",len(str)) # shows length of string
    print("2)",str[4])   # shows empty since it represnts space after s;nb: indices start from 0
    print("3)",str[-1]) #returns last character
    print("4)",str[:4])  #returns the first 4 characters not indices
   # print("5)",str[len(str)]) ---has an error
    print("6)",str[-6:])  # returns from index -6 to the last towards the right direction
    print("7)",str[len(str)-1]) # returns last character
    print("8)",str[-9:-7])  #returns characters -8 and -7 read towards the right
    print("9)",str[4:1])    #is empty i'm not sure why
    print("10)",str[-10:27]) #returns from character -10 to the last in right direction


main()
    
