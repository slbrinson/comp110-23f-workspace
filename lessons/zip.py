"""Combining two lists into a dictionary."""

__author__ = "730717721"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Creating a dictionary from two lists."""
    zip_dict = dict()
    if len(list1) == len(list2) and len(list1) != 0 and len(list2) != 0:
        zip_dict = {list1[elem]: list2[elem] for elem in range(len(list1))}
    else:
        zip_dict = dict()
    return zip_dict