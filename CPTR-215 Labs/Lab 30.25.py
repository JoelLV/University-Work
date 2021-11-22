def getMonthNumForFormula(month):
    """This function converts given month in a number that can be used for the Zeller's formula.

    >>> getMonthNumForFormula(2)
    14
    >>> getMonthNumForFormula(1)
    13
    >>> getMonthNumForFormula(3)
    3
    >>> getMonthNumForFormula(4)
    4
    >>> getMonthNumForFormula(5)
    5
    >>> getMonthNumForFormula(6)
    6
    >>> getMonthNumForFormula(7)
    7
    >>> getMonthNumForFormula(8)
    8
    >>> getMonthNumForFormula(9)
    9
    >>> getMonthNumForFormula(10)
    10
    >>> getMonthNumForFormula(11)
    11
    >>> getMonthNumForFormula(12)
    12
    """

    month_dic = {
        1 : 13,
        2 : 14,
        3 : 3,
        4 : 4,
        5 : 5,
        6 : 6,
        7 : 7,
        8 : 8,
        9 : 9,
        10 : 10,
        11 : 11,
        12 : 12
    }

    return month_dic[month]

def nameForDayOfWeekNumber(dayNumber):
    """This function converts the number given by the Zeller's rule to the name of the day.
    >>> nameForDayOfWeekNumber(7)
    'Sabbath'
    >>> nameForDayOfWeekNumber(1)
    'Sunday'
    >>> nameForDayOfWeekNumber(2)
    'Monday'
    >>> nameForDayOfWeekNumber(3)
    'Tuesday'
    >>> nameForDayOfWeekNumber(4)
    'Wednesday'
    >>> nameForDayOfWeekNumber(5)
    'Thursday'
    >>> nameForDayOfWeekNumber(6)
    'Friday'
    """
    day_dic = {
        7 : "Sabbath",
        1 : "Sunday",
        2 : "Monday",
        3 : "Tuesday",
        4 : "Wednesday",
        5 : "Thursday",
        6 : "Friday"
    }

    return day_dic[dayNumber]

def dayOfWeekForDate(year, month, day):
    """This function will accept three integers; year, month, and day respectively.
    This function will calculate the exact day of week given the date that was passed as parameters,
    and will return a string of the name of the day.  This function uses the Zeller's rule to calculate the day.
    >>> dayOfWeekForDate(2022, 1, 8)
    7
    >>> dayOfWeekForDate(2021, 9, 17)
    6
    >>> dayOfWeekForDate(2021, 10, 9)
    7
    >>> dayOfWeekForDate(2021, 8, 11)
    4
    >>> dayOfWeekForDate(2021, 7, 12)
    2
    >>> dayOfWeekForDate(2021, 6, 15)
    3
    >>> dayOfWeekForDate(2021, 3, 14)
    1
    >>> dayOfWeekForDate(1844, 10, 22)
    3
    >>> dayOfWeekForDate(2000, 2, 29)
    3
    >>> dayOfWeekForDate(2017, 9, 7)
    5
    """
    m = getMonthNumForFormula(month)

    if m == 13 or m == 14:
        year -= 1

    k = day
    D = year % 100
    C = year // 100
    num_day = k + ((13 * (m + 1)) // 5) + D + (D // 4) + (C // 4) - (2 * C)
    num_day %= 7

    if num_day == 0:
        num_day = 7

    return num_day

if __name__ == '__main__':
    import doctest
    doctest.testmod()