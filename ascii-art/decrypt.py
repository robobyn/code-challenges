# open and read text file

import ast


def read_file(txt_file):
    """Open and read text file."""

    open_file = open(txt_file, 'r')
    contents = open_file.read()

    return contents


def parse_string(txt_file):
    """Parse contents of read_file function.

       Args: a string that resembles a list of arrays.

       Output: An array of arrays."""

    readable_file = read_file(txt_file)

    split_str = readable_file.split("\n")

    parsed_contents = []

    for item in split_str:

        parsed_contents.append(ast.literal_eval(item))

    return parsed_contents


def create_matrix(width, height):
    """Takes integers as inputs for width and height to create matrix.

       Matrix output will be array of arrays containing 0 in each spot as a
       placeholder."""

    matrix = [[0 for x in range(width)] for y in range(height)]

    return matrix


def decrypt_ascii(txt_file, width, height):
    """Given a text file, height and width, return ascii art.

       Text file contains string that resembles array of arrays where 1st
       value represents x axis, 2nd value represents y axis, and 3rd value
       represents ASCII value of character to be printed in matrix.

       Output is printed ASCII art."""

    pos_and_chars = parse_string(txt_file)

    matrix = create_matrix(width, height)

    for array in pos_and_chars:

        x, y = array[0], array[1]
        char = chr(array[2])

        matrix[x][y] = char

    for array in matrix:

        print array


decrypt_ascii("ascii_array.txt", 100, 100)
