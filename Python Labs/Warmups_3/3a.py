# Define your function here.
def integer_to_reverse_binary(integer_value):
    """Function takes an integer and returns a string representing the given integer as a reverse binary number.
    >>> integer_to_reverse_binary(2)
    '01'
    >>> integer_to_reverse_binary(10)
    '0101'
    >>> integer_to_reverse_binary(91)
    '1101101'
    >>> integer_to_reverse_binary(380)
    '001111101'
    """
    binary_str = ''
    while integer_value > 0:
        binary_str += str(integer_value % 2)
        integer_value //= 2

    return binary_str

def reverse_string(input_string):
    """Function reverses and returns a new string representing the reverse of given string as parameter.
    >>> reverse_string('car')
    'rac'
    >>> reverse_string('pato')
    'otap'
    >>> reverse_string('')
    ''
    >>> reverse_string('laptop')
    'potpal'
    """
    reverse_str = ""
    for index in reversed(range(len(input_string))):
        reverse_str += input_string[index]
    
    return reverse_str

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    user_input = int(input())
    binary_num = integer_to_reverse_binary(user_input)
    binary_num = reverse_string(binary_num)

    print(binary_num)