"""EX04 - List Utils."""

__author__ = "730717721"


def all(input: list[int], single_num: int) -> bool:
    """Checking if all numbers in the list match a single given number."""
    all_idx: int = 0
    matches: bool = True

    if len(input) == 0:
        return False
    
    while all_idx < len(input):
        if single_num == input[all_idx] and len(input) != 0:
            matches = True
        else:
            return False
        all_idx += 1
    return matches
        

def max(input: list[int]) -> int:
    """Finding the highest valued number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    list_idx: int = 0
    max_num: int = int(input[0])

    while list_idx < len(input):
        current_num: int = int(input[list_idx])
        if (current_num > max_num):
            max_num = current_num
        list_idx += 1
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checking if the numbers in each list match at each index."""
    list_idx: int = 0
    matches: bool = True

    if len(list1) != len(list2):
        return False

    while list_idx < len(list1) and len(list2):
        if (list1[list_idx] == list2[list_idx]):
            matches = True
        else:
            return False
        list_idx += 1
    return matches