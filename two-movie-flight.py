"""Write a function that takes an integer flight_length (in minutes) and a list
of integers movie_lengths (in minutes) and returns a boolean indicating whether
there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory"""


def find_two_movies(flight_length, movie_lengths):
    """Determine whether two movie lengths exist that add up to flight length.

    Input: flight_length is int in minutes, movie_lengths is list of ints in
    minutes.

    Returns: Boolean value for whether or not 2 movie lengths exist that add
    up exactly to flight length."""

    seen = set()

    for i in range(len(movie_lengths)):

        current_movie_len = movie_lengths[i]
        second_mov_len_needed = flight_length - current_movie_len

        if second_mov_len_needed in seen:

            return True

        seen.add(current_movie_len)

    return False


print find_two_movies(135, [70, 120, 135, 90, 65])
print find_two_movies(200, [90, 120, 180, 100, 115])
print find_two_movies(200, [100, 120, 180, 115, 85])
