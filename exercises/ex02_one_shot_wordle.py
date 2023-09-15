"""EX02 - One Shot Wordle"""

__author__ = "730717721"

secret_word: str = "python"
secret_word_guess: str = input("What is your " + str(len(secret_word)) + "-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(secret_word_guess) != len(secret_word):
    incorrect_length: str = input("That was not " + str(len(secret_word)) + " letters! Try again: ")
    if len(secret_word_guess) == len(secret_word):
        print("Woo! You got it!")
        
if len(secret_word_guess) == len(secret_word) and secret_word_guess == secret_word:
    print("Woo! You got it!")
    exit()
else:
    print("Not quite. Play again soon!")
    exit()