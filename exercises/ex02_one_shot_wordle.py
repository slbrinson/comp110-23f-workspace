"""EX02 - One Shot Wordle"""

__author__ = "730717721"

secret_word: str = "python"
secret_word_guess: str = input(f"What is your {(len(secret_word))}-letter guess? ")

letter_idx: int = 0
emoji: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(secret_word_guess) != len(secret_word):
    new_guess: str = input(f"That was not {(len(secret_word))} letters! Try again: ")
    secret_word_guess = new_guess
    
while letter_idx < len(secret_word):
    if secret_word_guess[letter_idx] == secret_word[letter_idx]:
        emoji = emoji + GREEN_BOX
    else:
        emoji = emoji + WHITE_BOX
    letter_idx = letter_idx + 1

print(emoji)

if len(secret_word_guess) == len(secret_word) and secret_word_guess != secret_word:
    print("Not quite. Play again soon!")

if secret_word_guess or new_guess == secret_word:
    print("Woo! You got it!")