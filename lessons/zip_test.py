"""Test my zip function."""

__author__ = "730717721"

from lessons.zip import zip


def test_zip_length() -> None:
    """Testing on each list with one element each."""
    test_list: list[str, int] = ["Hello", 5]
    assert zip(test_list) == "Hello", 5