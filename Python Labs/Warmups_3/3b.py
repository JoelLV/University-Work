def fibonacci(n):
    """Function returns a number representing the index given as a paramenter in the fibonacci sequence
    >>> fibonacci(1)
    1
    >>> fibonacci(0)
    0
    >>> fibonacci(6)
    8
    >>> fibonacci(5)
    5
    >>> fibonacci(7)
    13
    >>> fibonacci(-10)
    -1
    """
    if n == 0:
        return 0
    elif n < 0:
        return -1
    else:
        curr_num = 1
        previous_num = 0
        for i in range(n - 1):
            temp_num = curr_num
            curr_num = curr_num + previous_num
            previous_num = temp_num
        return curr_num
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    start_num = int(input())
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))