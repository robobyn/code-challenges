def recurse_search(num, lst):
    while lst:

        if lst[0] == num:
            return True

        else:
            lst = lst[1:]
            recurse_search(num, lst)

    return False


def helper_function(num, lst):
    copy = lst

    if recurse_search(num, copy):
        return [idx for idx, element in enumerate(lst) if element == num][0]

    else:
        return -1
