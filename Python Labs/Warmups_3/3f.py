def isStrictlyIncreasing(list):
    """Function that returns true if the list of any type of variable that supports == and <= operators are ordered
    from lower to higher.
    >>> isStrictlyIncreasing([1, 2, 3, 4, 5, 6])
    True
    >>> isStrictlyIncreasing(['a', 'b', 'c', 'd'])
    True
    >>> isStrictlyIncreasing([3, 5, 1, 2])
    False
    >>> isStrictlyIncreasing([[1, 2, 3], [1, 2, 3, 4, 5]])
    True
    >>> isStrictlyIncreasing([True, True, False])
    False
    >>> isStrictlyIncreasing([False, True, True])
    False
    """

    for index in range(len(list) - 1):
        if list[index + 1] <= list[index]:
            return False
    else:
        return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()