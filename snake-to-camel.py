def snake_to_camel(var):
    """Convert a string in snake case to camel case.

    >>> snake_to_camel("hi_balloonicorn")
    'hiBalloonicorn'"""

    camel = ""

    while var:

        if var[0] != "_":
            camel += var[0]
            var = var[1:]

        else:
            camel += var[1].upper()
            var = var[2:]

    return camel

if __name__ == "__main__":
    import doctest
    doctest.testmod()
