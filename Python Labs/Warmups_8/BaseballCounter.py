from enum import Enum

class HalfInning(Enum):
    TOP = 0
    BOTTOM = 1

class BaseballCounter:
    def __init__(self, balls = 0, strikes = 0, outs = 0, half = HalfInning.TOP, inning = 1):
        """Initializes a BaseballCounter object
        """
        self.balls = balls
        self.strikes = strikes
        self.outs = outs
        self.half = half
        self.inning = inning

    def __repr__(self):
        """ Python executable representation of BaseballCounter class
        >>> BaseballCounter()
        BaseballCounter(0, 0, 0, HalfInning.TOP, 1)
        >>> BaseballCounter(1, 2, 3, HalfInning.BOTTOM, 4)
        BaseballCounter(1, 2, 3, HalfInning.BOTTOM, 4)
        >>> BaseballCounter(strikes = 3, outs = 6, inning = 10)
        BaseballCounter(0, 3, 6, HalfInning.TOP, 10)
        """
        return f"BaseballCounter({self.balls}, {self.strikes}, {self.outs}, HalfInning.{self.half.name}, {self.inning})"
    
    def __str__(self):
        """Human readable representation of BaseballCounter object
        >>> str(BaseballCounter())
        '0 balls, 0 strikes, 0 outs, top of the 1st inning'
        >>> str(BaseballCounter(1, 1, 1, HalfInning.BOTTOM, 4))
        '1 ball, 1 strike, 1 out, bottom of the 4th inning'
        >>> str(BaseballCounter(2, 2, 2, HalfInning.BOTTOM, 4))
        '2 balls, 2 strikes, 2 outs, bottom of the 4th inning'
        >>> str(BaseballCounter(inning = 2))
        '0 balls, 0 strikes, 0 outs, top of the 2nd inning'
        >>> str(BaseballCounter(inning = 3))
        '0 balls, 0 strikes, 0 outs, top of the 3rd inning'
        """
        object_str = ""
        endings = ["nothing", "st", "nd", "rd"]

        object_str += f"{self.balls} {'balls' if self.balls > 1 or self.balls == 0 else 'ball'}"
        object_str += f", {self.strikes} {'strikes' if self.strikes > 1 or self.strikes == 0 else 'strike'}"
        object_str += f", {self.outs} {'outs' if self.outs > 1 or self.outs == 0 else 'out'}"
        object_str += f", {'top' if self.half.value == 0 else 'bottom'} of the"
        object_str += f" {self.inning}{'th' if self.inning > 3 else endings[self.inning]} inning"

        return object_str
    
    def ball(self):
        """Counts number of balls, resets to 0 when reaches 4
        >>> obj = BaseballCounter()
        >>> obj.ball()
        >>> obj.balls
        1
        >>> obj = BaseballCounter(balls = 3)
        >>> obj.ball()
        >>> obj.balls
        0
        """
        self.balls += 1

        if self.balls == 4:
            self.new_batter()
    
    def strike(self):
        """Counts number of strikes, after 3, it resets to 0 and increases out by 1
        >>> obj = BaseballCounter()
        >>> obj.strike()
        >>> obj.strikes
        1
        >>> obj = BaseballCounter(strikes = 2)
        >>> obj.strike()
        >>> obj.strikes
        0
        >>> obj.outs
        1
        """
        self.strikes += 1

        if self.strikes == 3:
            self.out()
            self.new_batter()
    
    def new_batter(self):
        """Resets balls and strikes
        >>> obj = BaseballCounter(balls = 2, strikes = 1)
        >>> obj.new_batter()
        >>> obj.balls
        0
        >>> obj.strikes
        0
        """
        self.balls = 0
        self.strikes = 0
        
    def out(self):
        """Counts another out and calls new_batter() method to reset balls and strikes
        >>> obj = BaseballCounter(balls = 2, strikes = 2, outs = 2, half = HalfInning.BOTTOM)
        >>> obj.out()
        >>> obj.balls
        0
        >>> obj.strikes
        0
        >>> obj.outs
        0
        >>> obj.half.value
        0
        >>> obj.inning
        2
        >>> obj = BaseballCounter(balls = 2, strikes = 2, outs = 1, half = HalfInning.BOTTOM)
        >>> obj.out()
        >>> obj.balls
        2
        >>> obj.strikes
        2
        >>> obj.outs
        2
        >>> obj.half.value
        1
        """
        self.outs += 1

        if self.outs == 3:
            self.outs = 0
            self.half = HalfInning.TOP if self.half.value == 1 else HalfInning.BOTTOM
            self.new_batter()
            if self.half == HalfInning.TOP:
                self.inning += 1
                if self.inning == 10:
                    self.new_game()
    
    def new_game(self):
        """Resets every member field of BaseballCounter to default
        >>> obj = BaseballCounter(balls = 1, strikes = 1, outs = 1, half = HalfInning.BOTTOM, inning = 4)
        >>> obj.new_game()
        >>> obj.balls
        0
        >>> obj.strikes
        0
        >>> obj.outs
        0
        >>> obj.half.value
        0
        >>> obj.inning
        1
        """
        self.balls = 0
        self.strikes = 0
        self.outs = 0
        self.half = HalfInning.TOP
        self.inning = 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()