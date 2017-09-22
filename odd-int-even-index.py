def odd_int_even_index(elements):
    """Return all odd integers and elements with even index from input list.

    Args: List could contain elements other than ints.

    Challenge: Must use a generator expression with one line of code.

    >>> odd_int_even_index(["ball", 5, 1, "cat", 8, True, "no", 9, 4])
    ['ball', 5, 1, 8, 'no', 9, 4]

    >>> odd_int_even_index([7, 1, 7, 8, 0, 2, 8, 3, 4, 6, 5])
    [7, 1, 7, 0, 8, 3, 4, 5]
    """

    return list(element for index, element in enumerate(elements) if (type(element) is int and element % 2 !=0) or index % 2 == 0)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
