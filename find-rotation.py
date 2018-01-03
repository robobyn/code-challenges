"""In a mostly alphabetical list of words - find the 'rotation point' where the
list jumps back to an earlier point in the alphabet."""


def find_rotation(alpha_words):
    """Finds rotation point in list of words.

    Input: list of words that is mostly alphabetical but jumps back to an
    earlier letter in alphabet at an arbitrary index of list.

    Returns: Numerical index of list's rotation point.  Returns None if no
    rotation point found."""

    for i in range(len(alpha_words) - 1):

        current = alpha_words[i]
        next_word = alpha_words[i + 1]

        if current > next_word:
            return i + 1

    return None


print find_rotation([
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
])


def logn_find_rotation(alpha_words):
    """Finds rotation point in list of words - same as find_rotation() but
    uses binary search to do this in log(n) time."""

    if not alpha_words:
        return "No words in this list!"

    high_index = len(alpha_words) - 1
    low_index = 0
    mid_index = len(alpha_words) / 2

    while high_index > low_index:

        current = alpha_words[mid_index]
        prev_word = alpha_words[mid_index - 1]
        next_word = alpha_words[mid_index + 1]
        first_word = alpha_words[low_index]

        if prev_word > current:
            return mid_index

        elif next_word < current:
            return mid_index + 1

        if current < first_word:

            high_index = mid_index - 1

        else:

            low_index = mid_index + 1

        mid_index = (high_index + low_index) / 2

    return None


print logn_find_rotation([
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
])

print logn_find_rotation([
    'asymptote',
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
])
