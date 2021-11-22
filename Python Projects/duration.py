class Duration:
    def __init__(self, seconds_other, *args):
        """Constructs Duration object. Converts everything to seconds internally
        >>> Duration(23, 59, 59).total_seconds
        86399
        >>> Duration('1:30:00').total_seconds
        5400
        >>> Duration('1d8h45m10s').total_seconds
        117910
        >>> Duration('-45s').total_seconds
        -45
        >>> Duration(60).total_seconds
        60
        >>> Duration('-2h8m').total_seconds
        -7680
        >>> Duration('-0:00:34').total_seconds
        -34
        """
        total_seconds = 0
        if args:
            total_seconds += (seconds_other * 60 * 60)
            total_seconds += (args[0] * 60)
            total_seconds += args[1]
        elif isinstance(seconds_other, str):
            if ':' in seconds_other:
                if seconds_other[0] == '-':
                    items = seconds_other[1:].split(':')
                    is_negative = True
                else:
                    items = seconds_other.split(':')
                    is_negative = False
                
                hours = int(items[0])
                minutes = int(items[1])
                seconds = int(items[2])

                total_seconds += (hours * 60 * 60)
                total_seconds += (minutes * 60)
                total_seconds += seconds

                if is_negative:
                    total_seconds = -total_seconds
            else:
                number = ''
                days = 0
                hours = 0
                minutes = 0
                seconds = 0
                is_negative = False
                for index in range(len(seconds_other)):
                    if seconds_other[index] == '-':
                        is_negative = True
                        continue

                    if seconds_other[index] == 'd':
                        days = int(number)
                        number = ''
                    elif seconds_other[index] == 'h':
                        hours = int(number)
                        number = ''
                    elif seconds_other[index] == 'm':
                        minutes = int(number)
                        number = ''
                    elif seconds_other[index] == 's':
                        seconds = int(number)
                        number = ''
                    else:
                        number += seconds_other[index]
                
                total_seconds += days * 24 * 60 * 60
                total_seconds += hours * 60 * 60
                total_seconds += minutes * 60
                total_seconds += seconds

                if is_negative:
                    total_seconds = -total_seconds
        else:
            total_seconds = seconds_other

        self.total_seconds = total_seconds
    def __repr__(self):
        """Defines python-executable name for Duration class
        >>> Duration(23, 59, 59)
        Duration('23:59:59')
        >>> Duration(60)
        Duration('0:01:00')
        >>> Duration(-45)
        Duration('-0:00:45')
        >>> Duration(0)
        Duration('0:00:00')
        """
        repr_str = 'Duration(\'-' if self.total_seconds < 0 else 'Duration(\''
        second_conversion = self.convert_seconds()

        num_hours = str(abs(second_conversion[0]))
        num_minutes = str(abs(second_conversion[1])).rjust(2, '0')
        num_seconds = str(abs(second_conversion[2])).rjust(2, '0')

        repr_str = repr_str + f"{num_hours}:{num_minutes}:{num_seconds}\')"

        return repr_str

    def convert_seconds(self):
        """Returns a tuple containing the number of hours, minutes, and seconds of given seconds
        >>> Duration(45).convert_seconds()
        (0, 0, 45)
        >>> Duration('5h20m39s').convert_seconds()
        (5, 20, 39)
        >>> Duration('89:03:54').convert_seconds()
        (89, 3, 54)
        >>> Duration('-2h8m').convert_seconds()
        (2, 8, 0)
        """
        SECONDS_PER_HOUR = 3600
        SECONDS_PER_MINUTE = 60

        num_seconds = abs(self.total_seconds)
        num_hours = num_seconds // SECONDS_PER_HOUR
        num_seconds %= SECONDS_PER_HOUR
        num_minutes = num_seconds // SECONDS_PER_MINUTE
        num_seconds %= SECONDS_PER_MINUTE
        num_seconds = num_seconds

        return (num_hours, num_minutes, num_seconds)


    def __str__(self):
        """Creates human readable string for class Duration
        >>> str(Duration(60))
        '0:01:00'
        >>> str(Duration(-45))
        '-0:00:45'
        >>> str(Duration('6h56m'))
        '6:56:00'
        >>> str(Duration('1:30:12'))
        '1:30:12'
        """
        second_conversion = self.convert_seconds()
        num_hours = str(abs(second_conversion[0]))
        num_minutes = str(abs(second_conversion[1])).rjust(2, '0')
        num_seconds = str(abs(second_conversion[2])).rjust(2, '0')

        string_repr = f"{num_hours}:{num_minutes}:{num_seconds}"

        return '-' + string_repr if self.total_seconds < 0 else string_repr
    
    def __add__(self, other):
        """Overrides + operator for class Duration
        >>> Duration(10) + Duration(20)
        Duration('0:00:30')
        >>> Duration('2h') + Duration(10)
        Duration('2:00:10')
        >>> Duration('-45s') + Duration('15s')
        Duration('-0:00:30')
        """
        if isinstance(other, int):
            return Duration(self.total_seconds + other)
        else:
            return Duration(self.total_seconds + other.total_seconds)
    
    def __sub__(self, other):
        """Overrides - operator for class Duration
        >>> Duration(55) - Duration(10)
        Duration('0:00:45')
        >>> Duration('2d') - Duration('1d')
        Duration('24:00:00')
        >>> Duration('50m') - Duration('1h')
        Duration('-0:10:00')
        """
        if isinstance(other, int):
            return Duration(self.total_seconds - other)
        else:    
            return Duration(self.total_seconds - other.total_seconds)
    
    def __mul__(self, other):
        """Overrides * operator for Class Duration
        >>> Duration(10) * Duration(5)
        Duration('0:00:50')
        >>> Duration(-40) * Duration(10)
        Duration('-0:06:40')
        >>> Duration(10) * 5
        Duration('0:00:50')
        """
        if isinstance(other, int):
            return Duration(self.total_seconds * other)
        else:
            return Duration(self.total_seconds * other.total_seconds)
    
    def __eq__(self, other):
        """Overrides == operator for class Duration
        >>> Duration(34) == Duration(13)
        False
        >>> Duration('7s') == Duration(7)
        True
        >>> Duration('-0:00:34') == Duration(-34)
        True
        """

        return self.total_seconds == other.total_seconds
    
    def __lt__(self, other):
        """Overrides < operator for class Duration
        >>> Duration(10) < Duration(50)
        True
        >>> Duration(100) < Duration(23)
        False
        >>> Duration(-5) < Duration(0)
        True
        """

        return self.total_seconds < other.total_seconds
    
    def __le__(self, other):
        """Overrides <= operator for class Duration
        >>> Duration(190) <= Duration(190)
        True
        >>> Duration(65) <= Duration(15)
        False
        >>> Duration(200) <= Duration(210)
        True
        """
        if self < other or self == other:
            return True
        else:
            return False
    
    def __gt__(self, other):
        """Overrides > operator for class Duration
        >>> Duration(870) > Duration(20)
        True
        >>> Duration(90) > Duration(90)
        False
        >>> Duration(100) > Duration(200)
        False
        """
        if not self < other and not self == other:
            return True
        else:
            return False
    
    def __ge__(self, other):
        """Overrides >= operator for class Duration
        >>> Duration(90) >= Duration(90)
        True
        >>> Duration(100) >= Duration(10)
        True
        >>> Duration(12) >= Duration(20)
        False
        """

        if not self < other or self == other:
            return True
        else:
            return False
    
    def __ne__(self, other):
        """Overrides != operator for class Duration
        >>> Duration(100) != Duration(90)
        True
        >>> Duration(70) != Duration(70)
        False
        """

        if not self == other:
            return True
        else:
            return False
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()

