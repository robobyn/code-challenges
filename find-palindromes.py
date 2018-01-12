# number 47 and 74 add up to 121 - palindrome
# find numbers that add up to a palindrome of at least 1000
# find only the first 25 that meet above criteria
# start range of number possibilities from 100
# convert the number to a string flip numbers to get reverse
# each time through loop convert strings back to int
# add the number together
# check is palindrome and is > 1000
# append each number that meets criteria to list to return


def is_palindrome(num):
    """Checks any positive int to see if it is as palindrome.

    Params: num is any positive integer.  A number is considered a palindrome
    if it is the same forward as it is backward.

    Returns: Boolean value - True if palindrome, False if not.

    >>> is_palindrome(121)
    True

    >>> is_palindrome(45617)
    False

    >>> is_palindrome("tacocat")
    'Input must be positive int'
    """

    if type(num) != int or num < 0:
        return "Input must be positive int"

    str_num = str(num)
    reverse_num = str_num[::-1]

    if str(num) == reverse_num:
        return True

    return False


def find_palindromes():
    """Find all palindromes greater than 1000 that are the sum of two numbers
    that are the same forward and backward.

    Returns: list of ints that are palindromes > 1000 that are also the sum of
    two numbers that are the same forward and backward.

    >>> find_palindromes()
    [1111, 1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009, 2112, 3113, 4114, 5115, 6116, 7117, 8118, 9119, 1221, 2222, 3223, 4224, 5225, 6226, 7227]
    """

    palindromes = []
    seen = set()
    counter = 100

    while len(palindromes) < 25:

        str_counter = str(counter)
        rev_str_counter = str_counter[::-1]

        total = int(str_counter) + int(rev_str_counter)

        if is_palindrome(total) and total > 1000 and total not in seen:
            seen.add(total)
            palindromes.append(total)

        counter += 1

    return palindromes


if __name__ == "__main__":

    import doctest
    doctest.testmod()
