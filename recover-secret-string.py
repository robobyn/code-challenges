def recoverSecret(triplets):
    '''triplets is a list of triplets from the secrent string. Return the string.'''

    solution = []
    zero_index = set()
    one_index = set()
    two_index = set()

    for triplet in triplets:

        zero_index.add(triplet[0])
        one_index.add(triplet[1])
        two_index.add(triplet[2])

    for triplet in triplets:

        for char in triplet:

            if char in zero_index and char not in one_index and char not in two_index:
                solution.append(char)
                zero_index.remove(char)

    return solution


print recoverSecret([['t','u','p'], ['w','h','i'], ['t','s','u'], ['a','t','s'],
    ['h','a','p'], ['t','i','s'], ['w','h','s']])
