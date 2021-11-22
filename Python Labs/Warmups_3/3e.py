def inRange(lower_limit, upper_limit, n):
    """
    Function returns a boolean indicating whether a given num is between a range inclusively.
    >>> inRange(0, 6, 2)
    True
    >>> inRange(2, 10, 12)
    False
    >>> inRange(-2, 100, -1)
    True
    """

    if lower_limit <= n <= upper_limit:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    user_input = input().split()
    user_input = [int(num) for num in user_input]

    bound_input = input().split()
    lower_bound, upper_bound = [int(num) for num in bound_input]

    for num in user_input:
        if inRange(lower_bound, upper_bound, num):
            print(num,end=' ')