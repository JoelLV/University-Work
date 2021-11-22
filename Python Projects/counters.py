"""counters.py - Connectable Counters

Prof. O & CPTR-215
2021-11-03 fix errors
2021-10-31 implementation of Clock12 and Clock24 classes. Create Demos.
2021-10-28 implementation of Date class
2021-10-28 extract neighbor functionality
2021-10-27 add more polymorphism
2021-10-25 explore inheritance
2021-10-22 add doctests
2021-10-13 fix 12-hour clock using composition
2021-10-11 4-bit counter, 24-hour clock, (broken) 12-hour clock
2021-10-01 first draft

To Do:
- finish SC constructor (Completed)
- add starting value parameter to BC, LC, EC, & FLC (Completed)
- match existing classes to class diagram (Completed)
- create EnumCounter (?), Date, Clock12, and Clock24 classes (Completed)
- add lots of doctests (Completed)
"""

class Neighbor:
    """Neighbor represents an object that can:
    1) Connect to one or more neighbors (and be connected to also), and
    2) Notify those neighbors when it overflows,
        asking them to increment or reset themselves.
    """
    def __init__(self):
        self.increment_neighbors = []
        self.reset_neighbors = []
    def __str__(self):
        return (str(self.get_neighbor()) if self.get_neighbor() != None \
            else "") + str(self.get_value())
    def increment(self):
        self.notify_increment()
        self.notify_reset()
    def reset(self):
        pass
    def get_value(self):
        pass
    def add_increment(self, new_neighbor):
        if new_neighbor not in self.increment_neighbors:
            self.increment_neighbors.append(new_neighbor)
        return self
    def remove_increment(self, old_neighbor):
        if old_neighbor in self.increment_neighbors:
            self.increment_neighbors.remove(old_neighbor)
    def notify_increment(self):
        """Notifies all increment neighbors of overflow"""
        for neighbor in self.increment_neighbors:
            neighbor.increment()
    def add_reset(self, new_neighbor):
        if new_neighbor not in self.reset_neighbors:
            self.reset_neighbors.append(new_neighbor)
        return self
    def remove_reset(self, old_neighbor):
        if old_neighbor in self.reset_neighbors:
            self.reset_neighbors.remove(old_neighbor)
    def notify_reset(self):
        for neighbor in self.reset_neighbors:
            neighbor.reset()
    def get_neighbor(self):
        """Returns first neighbor, for printing"""
        return self.increment_neighbors[0] \
               if len(self.increment_neighbors) >= 1 \
               else None

class BoundedCounter(Neighbor):
    def __init__(self, lower_bound, upper_bound, start_value = None):
        """
        >>> bit = BoundedCounter(0, 1)
        >>> bit == None
        False
        >>> type(bit) == BoundedCounter
        True
        >>> bit.lower_bound
        0
        >>> bit.upper_bound
        1
        >>> bit.current_value
        0
        >>> bit = BoundedCounter(0, 1, 1)
        >>> bit.current_value
        1
        """
        super().__init__()
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.current_value = self.lower_bound if start_value == None else start_value
    def __repr__(self):
        """Provides python executable representation of object BoundedCOunter
        >>> repr(BoundedCounter(0, 9))
        'BoundedCounter(0, 9, 0)'
        >>> repr(BoundedCounter(0, 9, 2))
        'BoundedCounter(0, 9, 2)'
        """
        return f"BoundedCounter({self.lower_bound}, {self.upper_bound}, {self.current_value})"
    def increment(self):
        """
        >>> digit = BoundedCounter(0, 9)
        >>> digit.increment()
        >>> digit.current_value
        1
        >>> for _ in range(8): digit.increment()
        >>> digit.get_value()
        9
        >>> digit.increment()
        >>> digit.get_value()
        0
        """
        if self.current_value == self.upper_bound:
            self.current_value = self.lower_bound
            self.notify_increment()
            self.notify_reset()
        else:
            self.current_value += 1
    def reset(self):
        """Resets current value to the lower bound
        >>> counter = BoundedCounter(0, 9)
        >>> counter.increment()
        >>> counter.reset()
        >>> counter.get_value()
        0
        """
        self.current_value = self.lower_bound
    def get_value(self):
        """
        >>> counter = BoundedCounter(0, 9)
        >>> counter.get_value()
        0
        >>> counter.increment()
        >>> counter.get_value()
        1
        """
        return self.current_value

class ListCounter(BoundedCounter):
    def __init__(self, items, start_value = None):
        """Initializes ListCounter object
        >>> obj = ListCounter([1, 2, 3], 2)
        >>> obj = ListCounter([1, 2, 3])
        """
        start_value = items[0] if start_value == None else start_value
        self.items = tuple(items)
        super().__init__(0, len(self.items) - 1, items.index(start_value))
    def get_value(self):
        """Gets the value where the counter is currently at
        >>> obj = ListCounter([1, 2, 3, 4])
        >>> obj.get_value()
        1
        >>> obj.increment()
        >>> obj.get_value()
        2
        >>> obj = ListCounter([1, 2, 3, 4], 3)
        >>> obj.get_value()
        3
        """
        return self.items[super().get_value()]
    def __repr__(self):
        """Provides python executable representation of object listCounter
        >>> repr(ListCounter([1, 2, 3]))
        'ListCounter((1, 2, 3), 1)'
        >>> repr(ListCounter([1, 2, 3], 2))
        'ListCounter((1, 2, 3), 2)'
        """
        return f"ListCounter({self.items}, {self.get_value()})"
    
class FixedLengthCounter(BoundedCounter):
    def __init__(self, lo, hi, start_value = None, length = 2):
        """Initializes FixedLengthCounter object
        >>> obj = FixedLengthCounter(1, 5)
        >>> obj = FixedLengthCounter(1, 5, 2, 5)
        >>> obj = FixedLengthCounter(1, 5, 2)
        """
        super().__init__(lo, hi, start_value)
        self.length = length
    def get_value(self):
        """Returns a value representing where the pointer is at
        >>> obj = FixedLengthCounter(0, 5, 0, 2)
        >>> obj.get_value()
        '00'
        >>> obj.increment()
        >>> obj.get_value()
        '01'
        """
        return f"{super().get_value():0{self.length}}"
    def __repr__(self):
        """Python executable representation of FixedLengthCounter object
        >>> repr(FixedLengthCounter(0, 5, 1, 2))
        'FixedLengthCounter(0, 5, 1, 2)'
        >>> repr(FixedLengthCounter(0, 5))
        'FixedLengthCounter(0, 5, 0, 2)'
        >>> repr(FixedLengthCounter(0, 5, 4))
        'FixedLengthCounter(0, 5, 4, 2)'
        """
        return f"FixedLengthCounter({self.lower_bound}, {self.upper_bound}, {self.current_value}, {self.length})"
    
class StaticConnector(Neighbor):
    def __init__(self, string):
        """Initializes StaticConnector object
        >>> obj = StaticConnector('hello')
        >>> obj = StaticConnector('')
        """
        super().__init__()
        self.string = string
    def get_value(self):
        """Gets value of StaticConnector object
        >>> StaticConnector('something').get_value()
        'something'
        """
        return self.string
    def __repr__(self):
        """Provides Python executable representation of object StaticConnector
        >>> repr(StaticConnector('strong'))
        'StaticConnector("strong")'
        """
        return f"StaticConnector(\"{self.string}\")"

class Date():
    def __init__(self, year, month, day):
        """Initializes a Date object
        >>> obj = Date(2000, 3, 10)
        >>> obj.day.get_value()
        10
        >>> obj.month.get_value()
        3
        >>> obj.year.get_value()
        2000
        """
        self.year = BoundedCounter(1752, 9999, year)
        self.month = ListCounter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], month)
        self.day = get_bounded_counter(self.month.get_value(), self.year.get_value(), day)

        self.day.add_increment(self.month)
        self.month.add_increment(self.year)
        self.year.add_reset(self.month)
        self.month.add_reset(self.day)
    def __repr__(self):
        """Provides Python executable representation of object Date
        >>> repr(Date(2000, 3, 10))
        'Date(2000, 3, 10)'
        """
        return f'Date({self.year.get_value()}, {self.month.get_value()}, {self.day.get_value()})'
    def __str__(self):
        """Provides human readable representation of object Date
        >>> str(Date(2000, 1, 1))
        '2000-1-1'
        """
        return f"{self.year.get_value()}-{self.month.get_value()}-{self.day.get_value()}"
    def next_day(self):
        """Increments current day of Date object
        >>> date = Date(2000, 1, 1)
        >>> str(date)
        '2000-1-1'
        >>> str(date.next_day())
        '2000-1-2'
        >>> date = Date(2000, 1, 1)
        >>> for __ in range(31): date = date.next_day()
        >>> str(date)
        '2000-2-1'
        >>> for __ in range(29): date = date.next_day()
        >>> str(date)
        '2000-3-1'
        >>> for ___ in range(306): date = date.next_day()
        >>> str(date)
        '2001-1-1'
        >>> for __ in range(31): date = date.next_day()
        >>> str(date)
        '2001-2-1'
        >>> for __ in range(28): date = date.next_day()
        >>> str(date)
        '2001-3-1'
        """
        new_day = None
        previous_month = self.month.get_value()
        self.day.increment()

        if previous_month != self.month.get_value():
            new_day = get_bounded_counter(self.month.get_value(), self.year.get_value())
            self.day.remove_increment(self.month)
            self.month.remove_reset(self.day)
            self.day = new_day
            self.day.add_increment(self.month)
            self.month.add_reset(self.day)
        return self

class Clock12:
    def __init__(self, hours, minutes, ampm = 'AM'):
        """Constructs a Clock12 object
        >>> obj = Clock12(3, 5, 'PM')
        >>> obj = Clock12(3, 5)
        """
        ALL_HOURS = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        self.hour = ListCounter(ALL_HOURS, hours)
        self.minute = FixedLengthCounter(0, 59, minutes)
        self.colon = StaticConnector(":")
        self.space = StaticConnector(" ")
        self.ampm = ListCounter(["AM", "PM"], ampm)

        self.minute.add_increment(self.colon)
        self.colon.add_increment(self.hour)
        self.hour.add_increment(self.space)
        self.space.add_increment(self.ampm)

        self.ampm.add_reset(self.space)
        self.space.add_reset(self.hour)
        self.hour.add_reset(self.colon)
        self.colon.add_reset(self.minute)

    def __str__(self):
        """Returns a human readable string of object Clock12
        >>> obj = Clock12(12, 0)
        >>> str(obj)
        'AM 12:00'
        >>> obj = Clock12(6, 11, 'PM')
        >>> str(obj)
        'PM 6:11'
        >>> obj = Clock12(6, 9)
        >>> str(obj)
        'AM 6:09'
        >>> obj = Clock12(6, 10)
        >>> str(obj)
        'AM 6:10'
        """
        return str(self.minute)
    def next_minute(self):
        """Increments Clock12 object by one minute
        >>> obj = Clock12(12, 0)
        >>> str(obj)
        'AM 12:00'
        >>> obj.next_minute()
        >>> str(obj)
        'AM 12:01'
        >>> for __ in range(59): obj.next_minute()
        >>> str(obj)
        'AM 1:00'
        >>> for __ in range(660): obj.next_minute()
        >>> str(obj)
        'PM 12:00'
        >>> for __ in range(660 + 60): obj.next_minute()
        >>> str(obj)
        'AM 12:00'
        """
        self.minute.increment()

class Clock24:
    def __init__(self, hour, minutes):
        """Constructs a new Clock24 object
        >>> obj = Clock24(3, 5)
        """
        self.hour = FixedLengthCounter(0, 23, hour)
        self.colon = StaticConnector(":")
        self.minute = FixedLengthCounter(0, 59, minutes)

        self.minute.add_increment(self.colon)
        self.colon.add_increment(self.hour)

        self.hour.add_reset(self.colon)
        self.colon.add_reset(self.minute)
    def __str__(self):
        """Returns a human readable string representing Clock24 object
        >>> obj = Clock24(0, 0)
        >>> str(obj)
        '00:00'
        >>> obj = Clock24(1, 1)
        >>> str(obj)
        '01:01'
        >>> obj = Clock24(19, 18)
        >>> str(obj)
        '19:18'
        >>> obj = Clock24(10, 10)
        >>> str(obj)
        '10:10'
        """
        return str(self.minute)
    def next_minute(self):
        """Increments Clock24 object by 1 minute
        >>> obj = obj = Clock24(0, 0)
        >>> obj.next_minute()
        >>> str(obj)
        '00:01'
        >>> for __ in range(59): obj.next_minute()
        >>> str(obj)
        '01:00'
        >>> for __ in range(1380): obj.next_minute()
        >>> str(obj)
        '00:00'
        """
        self.minute.increment()

def get_bounded_counter(curr_month, curr_year, curr_day = 1):
        """Returns a Bounded Counter representing all possible days of current month
        >>> date = Date(2000, 1, 1)
        >>> get_bounded_counter(date.month.get_value(), date.year.get_value())
        BoundedCounter(1, 31, 1)
        >>> for __ in range(31): date = date.next_day()
        >>> get_bounded_counter(date.month.get_value(), date.year.get_value())
        BoundedCounter(1, 29, 1)
        >>> for __ in range(29 + 31): date = date.next_day()
        >>> get_bounded_counter(date.month.get_value(), date.year.get_value())
        BoundedCounter(1, 30, 1)
        >>> date = Date(2001, 2, 1)
        >>> get_bounded_counter(date.month.get_value(), date.year.get_value())
        BoundedCounter(1, 28, 1)
        """
        MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
        maximum_days = 0
        new_day = None
        if curr_month == 2:
                maximum_days = 29 if curr_year % 400 == 0 or curr_year % 4 == 0 and curr_year != 100 else 28
        elif curr_month in MONTHS_WITH_31_DAYS:
            maximum_days = 31
        else:
            maximum_days = 30
        
        new_day = BoundedCounter(1, maximum_days, curr_day)
        return new_day

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

    bit4 = FixedLengthCounter(0, 1, length = 2)
    plus = StaticConnector("+").add_increment(bit4)
    bit2 = BoundedCounter(0, 1).add_increment(plus)
    dash = StaticConnector("-").add_increment(bit2)
    bit1 = BoundedCounter(0, 1).add_increment(dash)
    for _ in range(20):
        print(bit1)
        bit1.increment()
    
    print("\nDemo for Date class:\n")

    date = Date(2000, 1, 1)
    print(f"Starting date = {date}\n")
    print(f"Today's date is {date}, tomorrow's date is {date.next_day()}")

    while(True):
        user_input = input("Enter a number to skip N days, Type E to exit: ")
        if user_input == 'E':
            break
        else:
            user_input = int(user_input)
            for __ in range(user_input):
                date.next_day()
            print(f"Current Date: {date}")
    
    print("\nDemo for Clock12 and Clock24 classes\n")

    clock12 = Clock12(12, 0)
    clock24 = Clock24(0, 0)

    print(f"Starting values for clock12 and clock24 = {clock12} | {clock24}\n")

    while(True):
        user_input = input("Enter a number to increment N minutes, Type E to exit: ")
        if user_input == 'E':
            break
        else:
            user_input = int(user_input)
            for __ in range(user_input):
                clock12.next_minute()
                clock24.next_minute()
            print(f"Current time in 12 hour and 24 hour formats: {clock12} | {clock24}")