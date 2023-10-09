"""EX04 - List Utils."""

__author__ = "730717721"

def all(input: list[int], single_num: int) -> bool:
    all_idx: int = 0
    matches: bool = True

    while all_idx < len(input):
        if single_num == input[all_idx]:
            matches = True
        else:
            return False
        all_idx += 1
    return matches
        
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
def is_equal(list1: list[int], list2: list[int]) -> bool:
    list1_idx: int = 0
    list2_idx: int = 0
    matches: bool = True

    while list1_idx and list2_idx < len(list1) and len(list2):
        if list1[list1_idx] == list2[list2_idx]:
            matches = True
        elif list1[list1_idx] != list2[list2_idx]:
            return False
        list1_idx += 1
        list2_idx += 1
    return matches