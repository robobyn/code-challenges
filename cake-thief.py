
def max_duffel_bag_value(cake_tuples, capacity):
    """Find max monetary value capacity of bag can hold.

    Params: cake_tuples represents weight of each cake at index 0, and
    monetary value of each cake at index 1.  Capacity represents the weight
    capacity of bag.  All values can be any non-negative int.

    Returns: Maximum monetary value possible given weights and values of cakes,
    and capacity of bag."""

    # possible_weights = {}

    # for cake in cake_tuples:

    #     weight = cake[0]
    #     value = cake[1]

    #     if weight < capacity:

    #         if weight not in possible_weights:
    #             possible_weights[weight] = [value]

    #         else:
    #             possible_weights[weight].append(value)

    # weight_combinations = {}

    possible_weights_and_values = {}

    for weight, value in cake_tuples:

        if weight < capacity:

            if weight not in possible_weights_and_values or\
               value > possible_weights_and_values[weight]:

                possible_weights_and_values[weight] = value

    return possible_weights_and_values

print max_duffel_bag_value([(7, 160), (3, 90), (2, 15), (2, 110), (45, 300)], 20)








