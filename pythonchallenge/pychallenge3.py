# solving python challenge 4 at www.pythonchallenge.com/pc/def/equality.html
import re


def find_bodyguards(long_string):
    """Find one small letter surrounded by exactly 3 large letters on each side."""

    # regex pattern exactly 3 uppercase 1 lowercase exactly 3 uppercase
    pattern = re.compile(r"[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+")

    # search for all matches to pattern in input string
    # returns list of all small letters that match pattern in string
    result = re.findall(pattern, long_string)

    print result

    return result

# text file contains very long string from python challenge page source code
open_file = open("bodyguards.txt")
a_long_string = open_file.read()

find_bodyguards(a_long_string)

closed_file = open_file.close()
