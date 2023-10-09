"""EX04 - List Utils."""

__author__ = "730717721"

def all(input: list[int], single_num: int) -> bool:
    all_idx: int = 0
    
    while all_idx <= len(input) - 1:
        if single_num == input[0]:
            return True
        all_idx += 1
        input[0] += 1
    else:
        return False
        
def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_num = input[0]
    while max_num < input[1]:
        return input[1]
    else:
        return max_num
    

def is_equal(list1: list[int] = list(), list2: list[int] = list()) -> bool:
