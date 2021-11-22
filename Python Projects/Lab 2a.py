def isLeapYear(year):
    """This method will take a year as a parameter and will check whether the year is a leap year or not.
        Returns a boolean.
        >>> isLeapYear(2020)
        True
        >>> isLeapYear(2019)
        False
        >>> isLeapYear(1700)
        False
        >>> isLeapYear(1600)
        True
    """
    is_leap_year = False
    
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
    else:
        if year % 4 == 0:
            is_leap_year = True
    
    return is_leap_year

def daysInMonth(month, year):
    """
    daysInMonth(month, year): This function will take a month in a number (ex. March = 3 or January = 1),
    and a year.  This function will return the number of days that the given month has.  Returns -1 if
    month entered is not valid.
    >>> daysInMonth(9, 2021)
    30
    >>> daysInMonth(10, 2021)
    31
    >>> daysInMonth(2, 2021)
    28
    >>> daysInMonth(2, 2020)
    29
    >>> daysInMonth(13, 2020)
    -1
    """
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    return -1

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

def startingDayOfWeek(month, year):
    """
    startingDayOfWeek(month, year): This function will return a number representing the day in which the month will start off.
    (ex. Monday = 1, Wednesday = 3).
    >>> startingDayOfWeek(9, 2021)
    4
    >>> startingDayOfWeek(10, 2021)
    6
    >>> startingDayOfWeek(8, 2021)
    1
    >>> startingDayOfWeek(1, 2022)
    7
    >>> startingDayOfWeek(8, 2022)
    2
    >>> startingDayOfWeek(3, 2022)
    3
    >>> startingDayOfWeek(9, 2022)
    5
    """
    m = getMonthNumForFormula(month)

    if m == 13 or m == 14:
        year -= 1
        
    k = 1
    D = year % 100
    C = year // 100
    num_day = k + ((13 * (m + 1)) // 5) + D + (D // 4) + (C // 4) - (2 * C) #Zeller's formula
    num_day %= 7

    if num_day == 0:
        num_day = 7

    return num_day

def getMonthNameFromMonthNumber(month_number):
    """This function converts the number of a month to its name.
    >>> getMonthNameFromMonthNumber(1)
    'January'
    >>> getMonthNameFromMonthNumber(3)
    'March'
    >>> getMonthNameFromMonthNumber(4)
    'April'
    >>> getMonthNameFromMonthNumber(10)
    'October'
    """
    month_dic = {
        1 : 'January',
        2 : 'February',
        3 : 'March',
        4 : 'April',
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August',
        9 : 'September',
        10 : 'October',
        11 : 'November',
        12 : 'December'
    }

    return month_dic[month_number]

def getHeadingForCalendar(month, year):
    """This function will return the heading needed for the calendar.
    >>> getHeadingForCalendar(5, 2021)
    '      May 2021'
    >>> getHeadingForCalendar(6, 2021)
    '     June 2021'
    >>> getHeadingForCalendar(10, 2021)
    '    October 2021'
    """
    MAX_NUM_SPACES_PER_ROW = 20

    month_str = getMonthNameFromMonthNumber(month)
    heading = month_str + " " + str(year)
    padding = (MAX_NUM_SPACES_PER_ROW - len(heading)) // 2
    heading = heading.rjust(padding + len(heading))
    
    return heading

def getSubheadingForCalendar():
    """
    This function returns the subheading for the calendar.  Includes abbreviations for the days of the week.
    >>> getSubheadingForCalendar()
    'Su Mo Tu We Th Fr Sa'
    """

    subheading = "Su Mo Tu We Th Fr Sa"

    return subheading

def getRowForCalendar(start_day, month, year):
    """
    This function returns a tuple containing a string that represents the day numbers of a week given the start day, and an integer that represents the next day number of the next week.
    The number of the month and year must also be passed in order to check the number of days in the given month and also to determine in which day to start counting.
    >>> getRowForCalendar(1, 9, 2021)
    ('          1  2  3  4', 5)
    >>> getRowForCalendar(12, 9, 2021)
    ('12 13 14 15 16 17 18', 19)
    >>> getRowForCalendar(5, 9, 2021)
    (' 5  6  7  8  9 10 11', 12)
    >>> getRowForCalendar(27, 2, 2022)
    ('27 28', 29)
    >>> getRowForCalendar(23, 2, 2020)
    ('23 24 25 26 27 28 29', 30)
    """
    day_limit = daysInMonth(month, year)
    start_position_in_calendar = startingDayOfWeek(month, year)
    curr_day = start_day
    row_str = ""

    for curr_position in range(1, 8):
        if curr_day == 1:
            if curr_position < start_position_in_calendar:
                row_str = row_str + "  "
            else:
                row_str = row_str + str(curr_day).rjust(2)
                curr_day += 1
        elif curr_day > day_limit:
            break
        else:
            row_str = row_str + str(curr_day).rjust(2)
            curr_day += 1
        
        if curr_position < 7 and curr_day <= day_limit:
            row_str = row_str + " "
    
    return row_str, curr_day

def monthCalendarFor(month, year):
    """
    This function prints out the calendar of a selected month.  Its parameters are month and year as integers respectively.
    >>> monthCalendarFor(9, 2021)
    '   September 2021\\n\
Su Mo Tu We Th Fr Sa\\n\
          1  2  3  4\\n\
 5  6  7  8  9 10 11\\n\
12 13 14 15 16 17 18\\n\
19 20 21 22 23 24 25\\n\
26 27 28 29 30\\n\\n'
    >>> monthCalendarFor(10, 2021)
    '    October 2021\\n\
Su Mo Tu We Th Fr Sa\\n\
                1  2\\n\
 3  4  5  6  7  8  9\\n\
10 11 12 13 14 15 16\\n\
17 18 19 20 21 22 23\\n\
24 25 26 27 28 29 30\\n\
31\\n'
    >>> monthCalendarFor(2, 2020)
    '   February 2020\\n\
Su Mo Tu We Th Fr Sa\\n\
                   1\\n\
 2  3  4  5  6  7  8\\n\
 9 10 11 12 13 14 15\\n\
16 17 18 19 20 21 22\\n\
23 24 25 26 27 28 29\\n\\n'
    """
    calendar_str = ""

    calendar_str = calendar_str + getHeadingForCalendar(month, year) + "\n"
    calendar_str = calendar_str + getSubheadingForCalendar() + "\n"

    curr_day = 1
    for row in range(6):
        calendar_row, next_week_day = getRowForCalendar(curr_day, month, year)
        calendar_str = calendar_str + calendar_row + "\n"
        curr_day = next_week_day
    
    return calendar_str

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    month = int(input("Please enter month in num: "))
    year = int(input("Please enter the year: "))

    print(monthCalendarFor(month, year))