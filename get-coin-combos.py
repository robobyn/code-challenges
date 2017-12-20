def get_coin_combos(amount, denominations):
    """Compute number of ways to make amount with coins in denominations.

    In: amount is an int representing a total amount of money.  denominations
    is a list of ints representing coin denominations to be used to add up
    to total amt of money.

    Out:  Return an int that is the count of different ways to make the amount
    of money using denominations listed.

    >>> get_coin_combos(4, [1, 2, 3])
    4
    """

    # create list where highest index is equivalent to value of amount input
    ways_of_doing_n_cents = [0] * (amount + 1)
    # set value of list index 0 to 1 as a starting point
    ways_of_doing_n_cents[0] = 1

    # loop through denominations list
    for coin in denominations:
        # loop through indices from current coin through end of list of ways
        for higher_amount in xrange(coin, amount + 1):
            # add value at index of prev coin values to current coin index
            # tracks number of combinations possible iteratively
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += \
                ways_of_doing_n_cents[higher_amount_remainder]

    return ways_of_doing_n_cents[amount]


print get_coin_combos(4, [1, 2, 3])
