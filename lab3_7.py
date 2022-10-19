#A program showing how to index arguments instead of letters

def main():
    std = ["Ali", 1, 2.5, "Elif", 2, 3.0] # std has 6 arguments
    print(std[0])  # 0 index will be Ali
    print(std[-1]) # prints last argument which is 3.0
    print(type(std[2]))  # prints data type of argument 2 which is 2.5 hence a float
    print(std[3])  #prints argument 3 which is Elif
    print(std[3][2]) # I am not quite sure why this one returns i 

main()
    
