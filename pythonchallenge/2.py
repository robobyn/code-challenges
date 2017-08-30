# solving python challenge 3 http://www.pythonchallenge.com/pc/def/ocr.html
from pprint import pprint


def find_rare_chars(long_string):
    """Function will count characters in a string and return dict.

       Dict will show key value pairs for each character and its count."""

    char_dict = {}

    for char in long_string:

        if char not in char_dict:
            char_dict[char] = 1

        else:
            char_dict[char] += 1

    return char_dict

open_file = open("long.txt")
a_long_string = open_file.read()
no_whitespace = a_long_string.rstrip()

pprint(find_rare_chars(no_whitespace))

closed_file = open_file.close()

# solution - rare characters are 'a, e, i, l, q, t, u, y'
# input 'equality' in url in place of ocr
