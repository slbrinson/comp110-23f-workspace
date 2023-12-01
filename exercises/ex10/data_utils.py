"""Dictionary related utility functions."""

__author__ = "730717721"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Define functin to read data from a stored file."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) of the list
    for elem in table:
        # for each dictionary (elem), get the value at key "header" and add that to result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column values
        result[key] = column_values(table, key)
    return result


def head(column_data: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table."""
    result: dict[str, list[str]] = {}
    if num_rows > 0:
        for column in column_data:
            column_head = []
            for value in column_data[column][:num_rows]:
                column_head.append(value)
            result[column] = column_head
    else:
        for column in column_data:
            result[column] = []
    return result


def select(column_data: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = column_data[column]
    return result


def concat(column_data1: dict[str, list[str]], column_data2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in column_data1:
        result[column] = column_data1[column]
    for column in column_data2:
        if column in result:
            result[column] += column_data2[column]
        else:
            result[column] = column_data2[column]
    return result


def count(vals_list: list[str]) -> dict[str, int]:
    """Count the number of times the value appears in the input list."""
    result: dict[str, int] = {}
    for value in vals_list:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result