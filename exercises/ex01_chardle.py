"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730717721"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_letter: str = input("Enter a single character: ")
if len(single_letter) != 1:
    print("Error: Character must be a single character.")
    exit()
instance_of_letter: int = 0

print("Searching for " + single_letter + " in " + five_character_word)

if single_letter == five_character_word[0]:
    print(single_letter + " found at index 0")
    instance_of_letter = instance_of_letter + 1

if single_letter == five_character_word[1]:
    print(single_letter + " found at index 1")
    instance_of_letter = instance_of_letter + 1

if single_letter == five_character_word[2]:
    print(single_letter + " found at index 2")
    instance_of_letter = instance_of_letter + 1

if single_letter == five_character_word[3]:
    print(single_letter + " found at index 3")
    instance_of_letter = instance_of_letter + 1

if single_letter == five_character_word[4]:
    print(single_letter + " found at index 4")
    instance_of_letter = instance_of_letter + 1

if instance_of_letter >= 1:
    print(str(instance_of_letter) + " instance of " + single_letter + " found in " + five_character_word)
    exit()

if instance_of_letter >= 2:
    print(str(instance_of_letter) + " instance of " + single_letter + " found in " + five_character_word)
    exit()

if instance_of_letter == 0:
    print("No instance of " + single_letter + " found in " + five_character_word)
    exit()