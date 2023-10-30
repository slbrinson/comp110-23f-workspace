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


def favorite_color(input: dict[str, str]) -> str:
    """Return the color that appears most."""
    colors_count = dict()
    popular_color = None
    for name in input:
        color = input[name]
        if color in colors_count:
            colors_count[color] += 1
        else:
            colors_count[color] = 1
        if popular_color is None or (colors_count[color] > colors_count[popular_color]):
            popular_color = color
    return popular_color


def count(input: list[str]) -> dict[str, int]:
    """Counting number of times items appear in list."""
    counts_dict = dict()
    for key in input:
        if key in counts_dict:
            counts_dict[key] += 1
        else:
            counts_dict[key] = 1
    return counts_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Returns a letter and words that begin with the letter."""
    alpha_dict = dict()
    for word in input:



    return alpha_dict


def update_attendance(days_and_students: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Return the students who were in attendance on certain days of the week."""