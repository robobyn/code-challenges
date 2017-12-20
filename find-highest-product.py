from itertools import islice


def find_highest_product(list_of_ints):
    """Given a list of ints find the highest product possible from 3 ints.

    Input: List of integers that will always have at least 3 ints.

    Return: Highest possible product of 3 of ints in list."""

    # greedy algorithm - assume first 2 ints are highest & lowest before looping
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    # tracking high and low product in case of negative nums in list
    high_product_2 = highest * lowest
    low_product_2 = highest * lowest

    high_product_3 = high_product_2 * list_of_ints[2]

    if len(list_of_ints) == 3:
        return high_product_3

    # use islice to avoid using additional space with python slicing
    for current in islice(list_of_ints, 2, None):

        # check if new highest product of 3
        high_product_3 = max(high_product_3,
                             current * high_product_2,
                             current * low_product_2)

        # check if new highest product of 2
        high_product_2 = max(high_product_2,
                             current * highest,
                             current * lowest)

        # check if new lowest product of 2
        low_product_2 = min(high_product_2,
                            current * highest,
                            current * lowest)

        # check if new highest num
        highest = max(current, highest)

        # check if new lowest num
        lowest = max(current, lowest)

    return high_product_3


print find_highest_product([1, -1, 0, 10, 6, 5])
print find_highest_product([-10, -10, 1, 3, 2])
