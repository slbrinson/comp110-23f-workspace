"""EX06 - Dictionary Functions."""

__author__ = "730717721"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values."""
    invert_dict = dict()
    for keys in input:
        value = input[keys]
        if value in invert_dict:
            raise KeyError("Duplicate entry!")
        invert_dict[value] = keys
    return invert_dict


def favorite_colors(input: dict[str, str]) -> str:
    """Return the color that appears most."""