def find_non_rep_dict(chr_str):
    """Find and return the first non-repeating character in a string.

    Input: A string of any number and any type of characters.

    Returns: The first non-repeating character in the string, or an empty string
    if there is no non-repeating character in the string."""

    seen = {}
    min_idx = None

    for idx, char in enumerate(chr_str):

        if char not in seen:
            seen[char] = [idx, 1]

        else:
            seen[char][1] += 1

    for char, idx_and_count in seen.iteritems():

        curr_idx = idx_and_count[0]
        count = idx_and_count[1]

        if (min_idx is None and count == 1) or \
           (min_idx is not None and curr_idx < min_idx and count == 1):

            min_idx = curr_idx

    if min_idx is not None:
        return chr_str[min_idx]

    else:
        return ""


print find_non_rep_dict("abcab")

print find_non_rep_dict("tooth")

print find_non_rep_dict("cab")

print find_non_rep_dict("xxxx")
