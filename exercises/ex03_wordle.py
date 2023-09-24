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