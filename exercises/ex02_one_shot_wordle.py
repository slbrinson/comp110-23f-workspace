"""EX02 - One Shot Wordle."""

__author__ = "730717721"

secret_word: str = "python"
secret_word_guess: str = input(f"What is your {(len(secret_word))}-letter guess? ")

letter_idx: int = 0
emoji: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(secret_word_guess) != len(secret_word):
    # asking for another guess when the length of the guess is not the length of the secret word
    new_guess: str = input(f"That was not {(len(secret_word))} letters! Try again: ")
    secret_word_guess = new_guess
    
while letter_idx < len(secret_word):
    if secret_word_guess[letter_idx] == secret_word[letter_idx]:
        # if the index at each place of the words match, a green box will print
        emoji = emoji + GREEN_BOX
    if secret_word_guess[letter_idx] != secret_word[letter_idx]:
        # indices of the guess are in the secret word but are not in the same index position, a yellow emoji will print
        letter_exists = False
        alternate_idx: int = 0
        
        while not(letter_exists) and alternate_idx < len(secret_word):
            if secret_word[alternate_idx] == secret_word_guess[letter_idx]:
                letter_exists = True
            else:
                alternate_idx = alternate_idx + 1
        if letter_exists is True:
            emoji = emoji + YELLOW_BOX

        # if the indices do not match and is not in the word at all, a white box will print
        else:
            emoji = emoji + WHITE_BOX
    letter_idx = letter_idx + 1

print(emoji)

if len(secret_word_guess) == len(secret_word) and secret_word_guess != secret_word:
    # the lengths of the guess and secret word match but they are not the same word
    print("Not quite. Play again soon!")

if secret_word_guess == secret_word:
    print("Woo! You got it!")