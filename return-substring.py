def return_longest_substring_length(character_str):
    """Returns the length of longest substring of unique characters."""

    substring = ""
    counter = 0
    highest_count = 0
    longest = ""

    for char in character_str:

        if char not in substring:
            counter += 1
            substring += char

        else:
            if counter > highest_count:
                highest_count = counter
                longest = substring
                char_idx = substring.index(char)
                substring = substring[(char_idx + 1):]
                counter = len(substring)

    return longest


print return_longest_substring_length("abcdaabbc")
print return_longest_substring_length("ghargggjiywq")
