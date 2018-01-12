def is_balanced(str_parens_braces_brackets):
    """Check a string to see if parens, brackets, and curly braces balanced.

    Params: A string containing any characters.  Any characters that are not
    '(', ')', '{', '}', '[', or ']' should be ignored. An empty string is
    considered balanced

    Returns: Boolean Value - True if balanced, False if not.

    >>> is_balanced("how[ are ( you ) ]")
    False

    >>> is_balanced("{ [ [ ] ] [ } ]")
    False

    >>> is_balanced("")
    True

    >>> is_balanced("not much]")
    False
    """

    stack = []

    opposites = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    for char in str_parens_braces_brackets:

        if char in opposites.keys():
            stack.append(char)

        elif char in opposites.values():

            if not stack:
                return False

            most_recent = stack.pop()

            if most_recent != opposites[most_recent]:
                return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
