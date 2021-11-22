def stringCleaner(user_string):
    """Cleans a string from every type of character except letters.
    >>> stringCleaner('1234')
    ''
    >>> stringCleaner('wording25')
    'wording'
    >>> stringCleaner('')
    ''
    >>> stringCleaner('El espanol es el mejor lenguage')
    'Elespanoleselmejorlenguage'
    """
    user_string = str(user_string)
    clean_str = ""
    for char in user_string:
        if (char.isalpha()):
            clean_str += char
    
    return clean_str

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    user_input = input()
    print(stringCleaner(user_input))