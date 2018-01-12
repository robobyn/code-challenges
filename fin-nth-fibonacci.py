"""Write a function fib() that a takes an integer n and returns the nth
Fibonacci number."""


def find_nth_fibonacci(n):
    """Finds and returns nth Fibonacci number.

    Input: Positive integer

    Returns: nth number in Fibonacci sequence - assumes series is 0-indexed."""

    if n < 0:
        raise ValueError("Negative index not allowed.")

    if n == 0 or n == 1:

        return n

    # start counter at n of 2 because need at least 2 prev ints for loop
    counter = 2
    # if n is 2 current will be 1 (result of adding 0 and 1)
    current = 1
    # previous number starts at 1
    prev = 1
    # second previous number starts at 0
    prev_prev = 0

    while counter < n:

        counter += 1
        prev_prev = prev
        prev = current
        current = prev_prev + prev

    return current


print find_nth_fibonacci(10)
print find_nth_fibonacci(0)
print find_nth_fibonacci(86)
print find_nth_fibonacci(6)
print find_nth_fibonacci(-5)
