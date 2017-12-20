def get_products_of_all_ints_except_at_index(int_lst):
    """For each num in list get product of every int in lst except current idx.

    Input: list of integers

    Returns: list of products for each int except the int at original index."""

    products = []

    for i in range(len(int_lst)):

        current = int_lst[:i] + int_lst[i + 1:]

        product = 1

        for num in current:

            product = product * num

        products.append(product)

    return products

print get_products_of_all_ints_except_at_index([1, 7, 3, 4])
print get_products_of_all_ints_except_at_index([5, 1, 4, 7, 0])
