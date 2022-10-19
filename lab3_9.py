# A program that asks user for input inform of a sentence
# The program breaks down the words in the sentence
# The program also calculates the length of each individual word

def main():
    
    sentence = input("Write a sentence: ")
    sen = sentence.split() # splits the sentence into its words
    
    for words in sen:
        print(words,end=' = ')  # prints the individual words on different lines
        print(len(words))       # prints the length of each word

main()
    
    
