"""'Sometimes (when I nest them (my parentheticals) too much (like this
    (and this))) they get confusing.'

Write a function that, given a sentence like the one above, along with the
position of an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of
    the first parenthesis), the output should be 79 (position of the last
    parenthesis)."""


def find_closing_paren(sentence, position):

    if sentence[position] != "(":
        return "The character at the position supplied is not an open paren!"

    p_to_skip = 0
    current_idx = position + 1

    for char in sentence[current_idx:]:

        if char == "(":
            p_to_skip += 1

        elif char == ")":
            if p_to_skip == 0:
                return current_idx

            else:
                p_to_skip -= 1

        if p_to_skip < 0:
            return "invalid parenthesis placements in sentence parameter."

        current_idx += 1


print find_closing_paren(
    "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.",
    10)
