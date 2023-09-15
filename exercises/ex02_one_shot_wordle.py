"""EX02 - One Shot Wordle"""

__author__ = "730717721"

secret_word: str = "python"
secret_word_guess: str = input("What is your " + str(int(len(secret_word))) + "-letter guess? ")

while len(secret_word_guess) != len(secret_word):
    incorrect_length: str = input("That was not " + str(int(len(secret_word))) + " letters! Try again: ")

if len(secret_word_guess) == len(secret_word) and secret_word_guess == secret_word:
    print("Woo! You got it!")
    exit()
else:
    print("Not quite. Play again soon!")
    exit()