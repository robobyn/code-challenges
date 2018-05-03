'''
Find the index of an item in a list using recursion.

Given a list of items:

    >>> lst = ["hey", "there", "you"]

You should have a function that returns the 0-based index of a sought item:

    >>> recursive_search("hey", lst)
    0

    >>> recursive_search("you", lst)
    2

If the item isn't in the list, return None:

    >>> recursive_search("folks", lst)
    None

Important: Solve this problem only with recursion; you cannot use a for or while loop in your solution!

Below we give you an empty function, recursive_index; please implement this method:


may need helper function to track index

use list slicing in our recursive function

base case one: nothing in list return None

base case two: found needle in haystack, return index

'''


def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    # function within function recurses and returns answer once search
    # either finds or does not find desired target
    def return_index(needle, haystack, indx_tracker):

        # if tracker exceeds the number of possible indices in input list
        # then target is not in the list
        if indx_tracker > (len(haystack) - 1):
            return None

        current = haystack[indx_tracker]

        if needle == current:
            return indx_tracker

        # recurse and feed current index plus one into function each time
        # target not found
        else:
            indx_tracker += 1
            return return_index(needle, haystack, indx_tracker)

    # return result of interior function
    return return_index(needle, haystack, 0)

######## Test code follows ########
# Some test cases, when you're ready (change False to True):
if True:
    # the "haystack" to be searched:
    lst = ['hey', 'there', 'you']

    print "We'll be searching through", lst
    # The tuple is a collection of words to be tried sequentially as the
    # "needle":
    expected = {'hey': 0, 'there': 1, 'you': 2, 'folks': None}
    # testing the things in the list, plus something not in it:
    for search_term in ('hey', 'there', 'you', 'folks'):

        result = recursive_index(search_term, lst)
        exp = expected[search_term]
        correct = "-- Correct." if result == exp else "-- Incorrect, expected %s." % exp
        print "==> recursive_index for " + search_term + " returned:", result, correct
