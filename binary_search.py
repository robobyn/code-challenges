def binary_search(num, sorted_arr):

    counter = 0
    high = len(sorted_arr)
    low = 0

    while high > low:
        counter += 1
        mid = (high + low) / 2

        if sorted_arr[mid] == num:
            print counter
            return True

        elif sorted_arr[mid] > num:
            high = mid - 1

        else:
            low = mid + 1

    print counter
    return False

print binary_search(5, [1, 3, 5, 7, 9])
print binary_search(7, [-5, -2, -1, 0, 10, 16, 100, 900])
