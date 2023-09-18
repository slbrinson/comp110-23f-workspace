"""EX02 - One Shot Wordle"""

__author__ = "730717721"

secret_word: str = "python"
secret_word_guess: str = input(f"What is your {(len(secret_word))}-letter guess? ")

letter_idx: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(secret_word_guess) != len(secret_word):
    new_guess: str = input(f"That was not {(len(secret_word))} letters! Try again: ")
    if len(new_guess) == len(secret_word) and new_guess != secret_word:
        print("Not quite. Play again soon!")
        exit()
    if new_guess == secret_word:
        print("Woo! You got it!")
        exit()

if len(secret_word_guess) == len(secret_word) and secret_word_guess != secret_word:
    print("Not quite. Play again soon!")
    exit()

while letter_idx < len(secret_word):
    if secret_word_guess or new_guess == secret_word:
        print(GREEN_BOX)
        letter_idx = letter_idx + 1
        print("Woo! You got it!")
        exit()