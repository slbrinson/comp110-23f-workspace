"""EX03 - Structured Wordle."""

__author__ = "730717721"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, single_char: str) -> bool:
    """Checking if the single character is in the word at any index."""
    assert len(single_char) == 1

    if single_char in word:
        return True
    else:
        return False

def emojified(guess: str, secret: str) -> str:
    """Will check indices and print corresponding colored emoji boxes."""
    assert len(guess) == len(secret)
    letter_idx: int = 0
    emoji: str = ""

    while letter_idx < len(secret):
        if contains_char(secret, guess[letter_idx]) is True and guess[letter_idx] == secret[letter_idx]:
            emoji = emoji + GREEN_BOX
        if contains_char(secret, guess[letter_idx]) is True and guess[letter_idx] != secret[letter_idx]:
            emoji = emoji + YELLOW_BOX
        if contains_char(secret, guess[letter_idx]) is False:
            emoji = emoji + WHITE_BOX
    letter_idx = letter_idx + 1
    return emoji


def input_guess(expected_len: int) -> str:
    """Prompting for correct word length of secret word."""
    guess: str = input(f"Enter a {expected_len} character word: ")

    while len(guess) != expected_len:
        if len(guess) != len(expected_len):
            guess = input(f"That wasn't {expected_len} chars! Try again: ")
        return input