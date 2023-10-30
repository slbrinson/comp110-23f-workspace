def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    alphabetized_dict = {}

    for word in input:
        if word:
            first_letter = word[0].lower()
            if 'a' <= first_letter <= 'z':
                if first_letter not in alphabetized_dict:
                    alphabetized_dict[first_letter] = [word]
                else:
                    current_list = alphabetized_dict[first_letter]
                    current_list += [word]
                    alphabetized_dict[first_letter] = current_list

    return alphabetized_dict

input = ['apple', 'banana', 'cherry', 'cat', 'dog', 'elephant', 'apple', 'fish']
result = alphabetizer(input)
print(result)


def favorite_colors(input: dict[str, str]) -> str:
    """Return the color that appears most."""
    colors_count: dict[str, int] = dict()
    popular_color: str() = ""
    for name in input:
        color = input[name]
        if color in colors_count:
            colors_count[color] += 1
        else:
            colors_count[color] = 1
        if popular_color == "" or (colors_count[color] > colors_count[popular_color]):
            popular_color = color
    return popular_color

# Example usage:
color_data = {
    'Alice': 'Blue',
    'Bob': 'Red',
    'Charlie': 'Blue',
    'David': 'Green',
    'Eve': 'Red',
    'Frank': 'Blue'
}

popular_color = favorite_colors(color_data)
print("The most popular color is:", popular_color)