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
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    
    return guess
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "snaggle"
    guess: str = ""
    turns: int = 1
    turns_count: int = 1

    while guess != secret and turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))

        if turns_count <= 6 and guess != secret:
            turns_count += 1
            turns += 1

        if turns_count <= 6 and guess == secret:
            turns_count += 1
            print(f"You won in {turns}/6 turns!")

        if turns > 6:
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()