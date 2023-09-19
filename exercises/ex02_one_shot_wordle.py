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
    #asking for another guess when the length of the guess is not the length of the secret word
    new_guess: str = input(f"That was not {(len(secret_word))} letters! Try again: ")
    secret_word_guess = new_guess
    
while letter_idx < len(secret_word):
    if secret_word_guess[letter_idx] == secret_word[letter_idx]:
        #if the index at each place of the words match, a green box will print
        emoji = emoji + GREEN_BOX
    if secret_word_guess[letter_idx] != secret_word[letter_idx]:
        #if the indices do not match, a white box will print
        emoji = emoji + WHITE_BOX

        #indices of the guess are in the secret word but are not in the same index position
        letter_exists: secret_word_guess(letter_idx) == [secret_word] and not secret_word_guess[letter_idx] == secret_word[letter_idx]
        alternate_idx: int = 0
        while not(letter_exists) and alternate_idx < len(secret_word):
            if alternate_idx == secret_word_guess[letter_idx]:
                
            else:
                alternate_idx = alternate_idx + 1
        if letter_exists == alternate_idx:
            emoji = emoji + YELLOW_BOX

    letter_idx = letter_idx + 1

print(emoji)

if len(secret_word_guess) == len(secret_word) and secret_word_guess != secret_word:
    #the lengths of the guess and secret word match but they are not the same word
    print("Not quite. Play again soon!")

if secret_word_guess == secret_word:
    print("Woo! You got it!")