def lemur(branches):
    """Return number of skips to get to las num given a list of numbers.

    List will contain 1's and 0's - skip only 1's.

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5"""

    jumps = 0

    # if only one branch no jumps needed
    if len(branches) == 1:
        return jumps

    # if 3 or fewer branches will never need more than 1 jump
    elif len(branches) <= 3:
        jumps += 1
        return jumps

    # when only 3 or fewer branches left will have number of jumps to return
    while len(branches) >= 3:

        jumps += 1

        # if the branch at furthest possible distance is not dead - jump to that
        if branches[2] != 1:
            branches = branches[2:]

        # if the branch at furthest possible distance is dead - jump to the prev
        else:
            branches = branches[1:]

    return jumps


if __name__ == "__main__":
    import doctest
    doctest.testmod()
