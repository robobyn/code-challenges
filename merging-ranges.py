def merge_meeting_times(list_of_time_ranges):
    """Create a list of times of day when all participants avail to meet.

    Input:  list of tuples where tuple[0] is each person's available start time
    and tuple[1] is each person's available end time.

    Return:  Condensed list of tuples showing range of times when everyone is
    available.

    >>> merge_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)
    [(0, 1), (3, 8), (9, 12)]
    """

    # sort input list to avoid passing through list more than once
    list_of_time_ranges.sort()

    # start list with just the first element
    merged_ranges = [list_of_time_ranges[0]]

    for i in range(1, len(list_of_time_ranges)):

        # compare last element of merged list to current element
        # if end time of last element is >= start time of current element,
        # can merge the two times and replace last element in merged list
        earlier = merged_ranges[-1]
        later = list_of_time_ranges[i]

        if earlier[1] >= later[0] and earlier[1] >= later[1]:
            pass

        elif earlier[1] >= later[0]:
            merged_ranges[-1] = (earlier[0], later[1])

        else:
            merged_ranges.append(later)

    return merged_ranges

print merge_meeting_times([(1, 3), (2, 4)])

print merge_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])

print merge_meeting_times([(1, 2), (2, 3)])

print merge_meeting_times([(1, 5), (2, 3), (4, 8), (10, 12), (9, 10)])

print merge_meeting_times([(1, 10), (2, 6), (3, 5), (7, 9)])
