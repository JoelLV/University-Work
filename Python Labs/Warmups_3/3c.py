def format_name(word_list):
    """Function that takes a string list as a parameter representing the words in a name and returns a string with the correct format.
    >>> format_name(['Joel', 'Lopez', 'Villarreal'])
    'Villarreal, J.L.'
    >>> format_name(['Gerardo', 'Reyes'])
    'Reyes, G.'
    >>> format_name([])
    ''
    """
    num_words = len(word_list)
    formated_name = ""

    if num_words == 3:
        formated_name += word_list[2] + ", "
        formated_name += word_list[0][0] + "." + word_list[1][0] + "."
    elif num_words == 2:
        formated_name += word_list[1] + ", "
        formated_name += word_list[0][0] + "."
    
    return formated_name

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    user_input = input()
    name_list = user_input.split()
    print(format_name(name_list))