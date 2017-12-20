def get_max_profit(stock_prices_yesterday):
    """Takes list of stock prices & returns best profit from 1 buy & 1 sell.

    Input: list of ints representing stock prices each minute of a day.

    Return: max profit possible by buying once and selling once during the
    day - must buy before selling."""

    # assume best option is diff between 1st and 2nd price until better found
    best = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    while len(stock_prices_yesterday) >= 2:

        first = stock_prices_yesterday[0]

        for i in range(1, len(stock_prices_yesterday) - 1):

            if stock_prices_yesterday[i] - first > best:

                best = stock_prices_yesterday[i] - first

        stock_prices_yesterday = stock_prices_yesterday[1:]

    return best

print get_max_profit([10, 7, 5, 8, 11, 9])
print get_max_profit([10, 9, 7, 4, 1, 0])


def get_max_profit_linear_time(stock_prices_yesterday):
    """Same problem but algorithm runs in O(n) time."""

    best_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    lowest_price = stock_prices_yesterday[0]

    for i in range(1, len(stock_prices_yesterday)):

        current_price = stock_prices_yesterday[i]
        current_profit = current_price - lowest_price

        best_profit = max(best_profit, current_profit)

        lowest_price = min(lowest_price, current_price)

    return best_profit

print get_max_profit([10, 7, 5, 8, 11, 9])
print get_max_profit([10, 9, 7, 4, 1, 0])
