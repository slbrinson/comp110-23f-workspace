"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730717721"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_letter: str = input("Enter a single character: ")
if len(single_letter) != 1:
    print("Error: Character must be a single character.")
    exit()
    
if single_letter == word[0]:
    print("Searching for " + single_letter + " in hello")
    print(single_letter + " found at index 0")

if single_letter == word[1]:
    print("Searching for " + single_letter + " in hello")
    print(single_letter + " found at index 1")

if single_letter == word[2]:
    print("Searching for " + single_letter + " in hello")
    print(single_letter + " found at index 2")

if single_letter == word[3]:
    print("Searching for " + single_letter + " in hello")
    print(single_letter + " found at index 3")

if single_letter == word[4]:
    print("Searching for " + single_letter + " in hello")
    print(single_letter + " found at index 4")