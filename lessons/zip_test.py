"""Test my zip function."""

__author__ = "730717721"

from lessons.zip import zip


def test_zip_list_length_one() -> None:
    """Test dict with one key and one value."""
    list1: list[str] = ["cupcake"]
    list2: list[int] = [5]
    test_list = {"cupcake": 5}
    assert zip(list1, list2) == test_list


def test_empty_zip() -> None:
    """Testing if list is empty."""
    list1: list[str] = []
    list2: list[int] = []
    test_list = {}
    assert zip(list1, list2) == test_list


def test_zip_list_length_two() -> None:
    """Test dict with two keys and two values."""
    list1: list[str] = ["cupcake", "pie"]
    list2: list[int] = [5, 7]
    test_list = {"cupcake": 5, "pie": 7}
    assert zip(list1, list2) == test_list