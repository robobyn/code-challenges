def bracket_validator(brackets):
    """Write an efficient function that tells us whether or not an input
    string's openers and closers are properly nested."""

    br_pairs = {"(": ")",
                "[": "]",
                "{": "}"}

    br_stack = []

    for bracket in brackets:
        if not br_stack and bracket not in br_pairs:
            return False

        elif bracket in br_pairs:
            br_stack.append(bracket)

        elif bracket in br_pairs.values():
            opener = br_stack.pop()

            if bracket != br_pairs[opener]:
                return False

    return True


print bracket_validator("{ [ ] ( ) }")
print bracket_validator("{ [ ( ] ) }")
print bracket_validator("{ [ }")
print bracket_validator("{ [ ( ] ) }")
