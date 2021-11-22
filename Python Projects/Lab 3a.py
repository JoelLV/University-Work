import math

THREE_DIGIT_SET_LIMIT = 12

def wordsFromNumber(user_num):
    """Function that returns a string representing given number
    in words.
    >>> wordsFromNumber(321)
    'three hundred twenty-one'
    >>> wordsFromNumber(104295)
    'one hundred four thousand two hundred ninety-five'
    >>> wordsFromNumber(0)
    'zero'
    >>> wordsFromNumber(548385893)
    'five hundred forty-eight million three hundred eighty-five thousand eight hundred ninety-three'
    >>> wordsFromNumber(865274953853)
    'eight hundred sixty-five billion two hundred seventy-four million nine hundred fifty-three thousand eight hundred fifty-three'
    >>> wordsFromNumber(100000004)
    'one hundred million four'
    """
    
    BASE_NUM = 1000

    num_str = ""

    if user_num == 0:
        num_str = "zero"
    
    else:
        curr_power = 10
        for digit_set in reversed(range(1, THREE_DIGIT_SET_LIMIT)):
            curr_three_digit_set = user_num // int(math.pow(BASE_NUM, curr_power))
            if curr_three_digit_set > 0:
                num_str += getThreeDigitNum(curr_three_digit_set) + getNameForThreeDigits(digit_set)
            user_num %= int(math.pow(BASE_NUM, curr_power))
            
            if curr_three_digit_set > 0 and user_num > 0:
                num_str += " "

            curr_power -= 1
    
    return num_str

def getNameForThreeDigits(n):
    """Function that returns a string representing the name of the three digit section.
    Accepts integers from 1 to 11.  Called in wordsFromNumber().
    >>> getNameForThreeDigits(2)
    ' thousand'
    >>> getNameForThreeDigits(3)
    ' million'
    >>> getNameForThreeDigits(4)
    ' billion'
    >>> getNameForThreeDigits(5)
    ' trillion'
    >>> getNameForThreeDigits(1)
    ''
    >>> getNameForThreeDigits(6)
    ' quadrillion'
    >>> getNameForThreeDigits(7)
    ' quintillion'
    >>> getNameForThreeDigits(10)
    ' octillion'
    """
    three_digit_dic = {
        1 : '',
        2 : ' thousand',
        3 : ' million',
        4 : ' billion',
        5 : ' trillion',
        6 : ' quadrillion',
        7 : ' quintillion',
        8 : ' sextillion',
        9 : ' septillion',
        10 : ' octillion',
        11 : ' nonillion'
    }

    return three_digit_dic[n]

def getThreeDigitNum(n):
    """Function that returns a string representing given number
    in words.  Only accepts three digits long.  Called in wordsFromNumber()
    >>> getThreeDigitNum(364)
    'three hundred sixty-four'
    >>> getThreeDigitNum(43)
    'forty-three'
    >>> getThreeDigitNum(9)
    'nine'
    >>> getThreeDigitNum(400)
    'four hundred'
    >>> getThreeDigitNum(690)
    'six hundred ninety'
    >>> getThreeDigitNum(104)
    'one hundred four'
    >>> getThreeDigitNum(113)
    'one hundred thirteen'
    >>> getThreeDigitNum(810)
    'eight hundred ten'
    """

    num_str = ""
    first_digit = n // 100
    n %= 100
    second_digit = n // 10
    n %= 10
    third_digit = n

    if first_digit > 0:
        num_str += getNameForSingleDigit(first_digit) + " hundred"

    if first_digit > 0 and second_digit > 0:
        num_str += " "

    if second_digit > 0:
        if 10 < (second_digit * 10) + third_digit < 20:
            num_str += getNameForSecondDigitLessThanTwenty(10 + third_digit)
            
            return num_str
        else:
            num_str += getNameForSecondDigit(second_digit)

    if second_digit > 0 and third_digit > 0:
        num_str += "-"
    elif first_digit > 0 and third_digit > 0:
        num_str += " "

    if third_digit > 0:
        num_str += getNameForSingleDigit(third_digit)

    return num_str

def getNameForSecondDigit(n):
    """Function that returns the name of multiples of ten from 20 to 90.  Called in getThreeDigitNum().
    >>> getNameForSecondDigit(2)
    'twenty'
    >>> getNameForSecondDigit(3)
    'thirty'
    >>> getNameForSecondDigit(8)
    'eighty'
    >>> getNameForSecondDigit(6)
    'sixty'
    >>> getNameForSecondDigit(9)
    'ninety'
    """

    two_digit_dic = {
        1 : 'ten',
        2 : 'twenty',
        3 : 'thirty',
        4 : 'forty',
        5 : 'fifty',
        6 : 'sixty',
        7 : 'seventy',
        8 : 'eighty',
        9 : 'ninety',
    }

    return two_digit_dic[n]

def getNameForSecondDigitLessThanTwenty(n):
    """Function that returns the name of numbers that are less than 20 but more than 10.  Called in getThreeDigitNum()
    >>> getNameForSecondDigitLessThanTwenty(13)
    'thirteen'
    >>> getNameForSecondDigitLessThanTwenty(18)
    'eighteen'
    >>> getNameForSecondDigitLessThanTwenty(19)
    'nineteen'
    >>> getNameForSecondDigitLessThanTwenty(12)
    'twelve'
    >>> getNameForSecondDigitLessThanTwenty(11)
    'eleven'
    """

    two_digit_dic = {
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen'
    }

    return two_digit_dic[n]

def getNameForSingleDigit(n):
    """Function that returns the name of numbers that are less than 10.  Called in getThreeDigitNum()
    >>> getNameForSingleDigit(9)
    'nine'
    >>> getNameForSingleDigit(1)
    'one'
    >>> getNameForSingleDigit(2)
    'two'
    >>> getNameForSingleDigit(9)
    'nine'
    >>> getNameForSingleDigit(0)
    'zero'
    """

    one_digit_dic = {
        0 : 'zero',
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine'
    }

    return one_digit_dic[n]

if __name__ == '__main__':
    import doctest
    doctest.testmod()