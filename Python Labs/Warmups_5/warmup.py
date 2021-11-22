"""date.py
Prof. O & CPTR-215
2021-09-29
2021-09-27 first draft
"""

class Date:
    def months_with_31_days(self):
        months = [1, 3, 5, 7, 8, 10, 12]

        return months
        
    def previous_day(self):
        """Returns a new Date object that represents the previous day
        given Date object.
        >>> Date(2021, 9, 30).previous_day()
        Date(2021, 9, 29)
        >>> Date(2021, 11, 25).previous_day()
        Date(2021, 11, 24)
        >>> Date(2022, 1, 1).previous_day()
        Date(2021, 12, 31)
        >>> Date(2021, 3, 1).previous_day()
        Date(2021, 2, 28)
        >>> Date(2020, 3, 1).previous_day()
        Date(2020, 2, 29)
        >>> Date(2021, 9, 1).previous_day()
        Date(2021, 8, 31)
        >>> Date(2021, 7, 1).previous_day()
        Date(2021, 6, 30)
        """

        if self.day == 1:
            if self.month == 3:
                if self.is_leap_year():
                    previous_day = 29
                else:
                    previous_day = 28
                previous_month = 2
                previous_year = self.year
            elif self.month == 1:
                previous_day = 31
                previous_month = 12
                previous_year = self.year - 1
            elif self.month - 1 in self.months_with_31_days():
                previous_day = 31
                previous_month = self.month - 1
                previous_year = self.year
            else:
                previous_day = 30
                previous_month = self.month - 1
                previous_year = self.year
        else:
            previous_month = self.month
            previous_day = self.day - 1
            previous_year = self.year

        previous_date = Date(previous_year, previous_month, previous_day)

        return previous_date
    
    def next_day(self):
        """Returns a new Date object that represents the next day of self.
        >>> Date(2021, 9, 29).next_day()
        Date(2021, 9, 30)
        >>> Date(2021, 9, 30).next_day()
        Date(2021, 10, 1)
        >>> Date(2021, 10, 31).next_day()
        Date(2021, 11, 1)
        >>> Date(2021, 12, 31).next_day()
        Date(2022, 1, 1)
        >>> Date(2021, 2, 28).next_day()
        Date(2021, 3, 1)
        >>> Date(2020, 2, 29).next_day()
        Date(2020, 3, 1)
        >>> Date(2021, 10, 30).next_day()
        Date(2021, 10, 31)
        >>> Date(2020, 2, 28).next_day()
        Date(2020, 2, 29)
        >>> Date(2020, 7, 31).next_day()
        Date(2020, 8, 1)
        >>> Date(3182, 12, 14).next_day()
        Date(3182, 12, 15)
        """
        if self.month == 2:
            if self.is_leap_year():
                if self.day == 29:
                    next_day = 1
                    next_month = 3
                    next_year = self.year
                else:
                    next_day = self.day + 1
                    next_month = self.month
                    next_year = self.year
            else:
                if self.day == 28:
                    next_day = 1
                    next_month = 3
                    next_year = self.year
                else:
                    next_day = self.day + 1
                    next_month = self.month
                    next_year = self.year
        elif self.month == 12:
            if self.day == 31:
                next_day = 1
                next_month = 1
                next_year = self.year + 1
            else:
                next_day = self.day + 1
                next_month = self.month
                next_year = self.year
        elif self.month in self.months_with_31_days():
            if self.day == 31:
                next_day = 1
                next_month = self.month + 1
                next_year = self.year
            else:
                next_day = self.day + 1
                next_month = self.month
                next_year = self.year
        else:
            if self.day == 30:
                next_day = 1
                next_month = self.month + 1
                next_year = self.year
            else:
                next_day = self.day + 1
                next_month = self.month
                next_year = self.year
        
        next_date = Date(next_year, next_month, next_day)

        return next_date

    def equals(self, other):
        """Returns a boolean representing whether two date objects represent
        the same date.
        >>> Date(2021, 10, 9).equals(Date(2021, 10, 9))
        True
        >>> Date(2021, 9, 9).equals(Date(2021, 8, 19))
        False
        >>> Date(2021, 2, 9).equals(Date(2021, 2, 8))
        False
        >>> Date(2020, 9, 9).equals(Date(2021, 9, 9))
        False
        >>> Date(2020, 8, 10).equals(Date(2020, 9, 10))
        False
        """

        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        else:
            return False
    
    def before(self, other):
        """Returns a boolean representing whether self is before given date
        >>> Date(2021, 9, 29).before(Date(2021, 9, 30))
        True
        >>> Date(2021, 9, 2).before(Date(2021, 9, 30))
        True
        >>> Date(2020, 12, 31).before(Date(2021, 1, 1))
        True
        >>> Date(2021, 2, 28).before(Date(2021, 3, 1))
        True
        >>> Date(2020, 2, 29).before(Date(2020, 3, 1))
        True
        >>> Date(2020, 10, 9).before(Date(2020, 10, 31))
        True
        >>> Date(2021, 9, 30).before(Date(2021, 10, 1))
        True
        >>> Date(2021, 7, 31).before(Date(2021, 8, 1))
        True
        """
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                if self.day < other.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def after(self, other):
        """Returns a boolean representing whether self represents the Date after
        given date.
        >>> Date(2021, 9, 30).after(Date(2021, 9, 29))
        True
        >>> Date(2021, 9, 29).after(Date(2021, 9, 30))
        False
        >>> Date(2021, 9, 2).after(Date(2021, 9, 30))
        False
        >>> Date(2022, 1, 1).after(Date(2021, 12, 31))
        True
        >>> Date(2021, 3, 1).after(Date(2021, 2, 28))
        True
        >>> Date(2020, 3, 1).after(Date(2020, 2, 29))
        True
        >>> Date(2020, 10, 9).after(Date(2020, 10, 31))
        False
        """
        
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                if self.day > other.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __init__(self, year, month, day):
        """Initializes a date given a year, month, and day.
        >>> today = Date(2021, 9, 27)
        >>> today.day
        27
        >>> Date(1776, 7, 4).year
        1776
        """
        self.year = year
        self.month = month
        self.day = day
    def day_of_week(self):
        """Determines the day of the week self falls on. 1 = Sun thru 7 = Sat.
        >>> today = Date(2021, 9, 27)
        >>> today.day_of_week()
        2
        >>> Date(2021, 9, 25).day_of_week()
        7
        >>> Date(1776, 7, 4).day_of_week()
        5
        """
        if self.month < 3:
            m = self.month + 12
            y = self.year - 1
        else:
            m = self.month
            y = self.year
        dow = (self.day + (13 * (m + 1)) // 5 + \
               y + y // 4 - y //  100 + y // 400) % 7
        return 7 if dow == 0 else dow
    def __str__(self):
        """Returns a human-readable string representation of self
        in MMM d, yyyy format.
        >>> Date(2000, 1, 1).__str__() # not common
        'Jan 1, 2000'
        >>> str(Date(2021, 9, 27))
        'Sep 27, 2021'
        >>> independence = Date(1776, 7, 4)
        >>> print(independence)
        Jul 4, 1776
        """
        month_name = "BAD Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()[self.month]
        return f"{month_name} {self.day}, {self.year}"
    def __repr__(self):
        """Returns a string that would evaluate to an identical Date object.
        >>> Date(2021, 9, 29).__repr__() # not common
        'Date(2021, 9, 29)'
        >>> Date(1970, 12, 31)
        Date(1970, 12, 31)
        >>> repr(Date(1984, 2, 20))
        'Date(1984, 2, 20)'
        """
        return f"Date({self.year}, {self.month}, {self.day})"
    def is_leap_year(self):
        """Determines whether self is in a leap year.
                    Truth Table
            4s place  2s place  1s place
             div 4 | div 100 | div 400 | leap?
            -------+---------+---------+-------
               0         0         0       0
               0         0         1       X
               0         1         0       X
               0         1         1       X
               1         0         0       1
               1         0         1       X
               1         1         0       0
               1         1         1       1
        >>> Date(2021, 9, 29).is_leap_year()
        False
        >>> Date(1984, 4, 27).is_leap_year()
        True
        >>> Date(2000, 1, 1).is_leap_year()
        True
        >>> Date(1900, 11, 30).is_leap_year()
        False
        """
        return self.year % 400 == 0 or \
               (self.year % 4 == 0 and self.year % 100 != 0)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
