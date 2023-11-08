"""EX07 - Dictionary Functions Test."""

__author__ = "730717721"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# three tests for invert
def test_empty_invert() -> None:
    """Testing if invert is empty."""
    input: dict[str, str] = []
    test_dict = {}
    assert invert(input) == test_dict


def test_invert() -> None:
    """Testing if invert is working."""
    input: dict[str, str] = {"hello": "goodbye"}
    expected_dict = {"goodbye": "hello"}
    assert invert(input) == expected_dict


def test_invert_two_items() -> None:
    """Testing if invert is working for multiple inverts."""
    input: dict[str, str] = {"hello": "goodbye", "happy": "birthday"}
    expected_dict = {"goodbye": "hello", "birthday": "happy"}
    assert invert(input) == expected_dict


# three tests for favorite_color
def test_empty_favorite_color() -> None:
    """Testing if favorite_color is empty."""
    input: dict[str, str] = []
    expected_fav_color = ""
    assert favorite_color(input) == expected_fav_color


def test_favorite_color() -> None:
    """Testing if favorite_color is working."""
    input: dict[str, str] = {"sam": "black", "shane": "blue", "bailee": "blue"}
    expected_fav_color = "blue"
    assert favorite_color(input) == expected_fav_color


def test_favorite_color_one_color() -> None:
    """Testing if favorite_color is working with one color each."""
    input: dict[str, str] = {"sam": "black", "shane": "blue", "bailee": "orange"}
    expected_fav_color = "black"
    assert favorite_color(input) == expected_fav_color


# three tests for count
def test_empty_count() -> None:
    """Testing if count is empty."""
    input: list[str] = ""
    expected_count = {}
    assert count(input) == expected_count


def test_count() -> None:
    """Testing if count is working for one letter."""
    input: list[str] = "p"
    expected_count = {"p": 1}
    assert count(input) == expected_count


def test_empty_count_one_word() -> None:
    """Testing if count is working for a word."""
    input: list[str] = "pie"
    expected_count = {"p": 1, "i": 1, "e": 1}
    assert count(input) == expected_count


# three tests for alphabetizer
def test_empty_alphabetizer() -> None:
    """Testing if alphabetizer is empty."""
    input: list[str] = ""
    expected_output = {}
    assert alphabetizer(input) == expected_output


def test_alphabetizer() -> None:
    """Testing if alphabetizer is working with one word."""
    input: list[str] = ["hello"]
    expected_output = {"h": ["hello"]}
    assert alphabetizer(input) == expected_output


def test_alphabetizer_two_words() -> None:
    """Testing if alphabetizer is working with multiple words."""
    input: list[str] = ["hello", "dog", "happy", "dandelion"]
    expected_output = {"h": ["hello", "happy"], "d": ["dog", "dandelion"]}
    assert alphabetizer(input) == expected_output


# three tests for update_attendance
def test_update_attendance() -> None:
    """Testing if update_attendance is working for multiple days."""
    attendance_log: dict[str, list[str]] = {"Monday": "Sam"}
    day: str = "Tuesday"
    student: str = "Sam"
    expected_attendance_log = {"Monday": "Sam", "Tuesday": ["Sam"]}
    assert update_attendance(attendance_log, day, student) == expected_attendance_log


def test_update_attendance_add_student() -> None:
    """Testing if update_attendance is working for adding student."""
    attendance_log: dict[str, list[str]] = {"Monday": "Sam"}
    day: str = "Tuesday"
    student: str = "Bailee"
    expected_attendance_log = {"Monday": "Sam", "Tuesday": ["Bailee"]}
    assert update_attendance(attendance_log, day, student) == expected_attendance_log


def test_update_attendance_add_student_and_day() -> None:
    """Testing if update_attendance is working for adding student and a day."""
    attendance_log: dict[str, list[str]] = {"Monday": "Sam"}
    day: str = "Tuesday"
    student: str = "Sam", "Bailee"
    expected_attendance_log = {"Monday": "Sam", "Tuesday": [("Sam", "Bailee")]}
    assert update_attendance(attendance_log, day, student) == expected_attendance_log