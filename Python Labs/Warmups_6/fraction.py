"""
Fractions
Prof. O & CPTR-215
2021-10-06 first draft
"""

class Fraction:
    def __init__(self, numerator = 1, denominator = 1):
        """Initializes a fraction
        >>> one_third = Fraction(1, 3)
        >>> one_as_fraction = Fraction(2)
        """
        a, b = numerator, denominator

        # Simplify using the Euclidean algorithm
        # https://en.wikipedia.org/wiki/Greatest_common_divisor#Euclidean_algorithm
        while b != 0:
            a, b = b, a % b
        self.numerator = numerator // a
        self.denominator = denominator // a
    
    def __repr__(self):
        """Python-executable representation
        >>> one_third = Fraction(1, 3)
        >>> one_third
        Fraction(1, 3)
        >>> Fraction(2, 4)
        Fraction(1, 2)
        >>> Fraction(768, 1024)
        Fraction(3, 4)
        >>> Fraction(3)
        Fraction(3)
        """
        if self.denominator == 1:
            return f"Fraction({self.numerator})"
        else:
            return f"Fraction({self.numerator}, {self.denominator})"
    
    def __str__(self):
        """Human-readable representation, num/dem
        >>> print(Fraction(1, 2))
        1/2
        >>> print(Fraction(1, 2) + Fraction(1, 2))
        1
        >>> print(Fraction(2, 3) + Fraction(4, 3))
        2
        """
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 \
               else str(self.numerator)
    
    def __add__(self, other):
        """
        >>> Fraction(1, 2) + Fraction(1, 3)
        Fraction(5, 6)
        >>> half = Fraction(1, 2)
        >>> third = Fraction(1, 3)
        >>> half + third # same as half.__add__(third), and also Fraction.__add__(half, third)
        Fraction(5, 6)
        >>> Fraction(1, 4) + Fraction(2, 8)
        Fraction(1, 2)

        """
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)
    
    def __eq__(self, other):
        """Overrides == operator for Fraction class
        >>> Fraction(1, 2) == Fraction(1, 2)
        True
        >>> Fraction(2, 4) == Fraction(1, 2)
        True
        >>> Fraction(1, 3) == Fraction(1, 4)
        False
        """
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        else:
            return False

    def __lt__(self, other):
        """Overrides < operator for Fraction class
        >>> Fraction(3, 2) < Fraction(1, 2)
        False
        >>> Fraction(4, 2) < Fraction(5, 2)
        True
        >>> Fraction(1, 8) < Fraction(1, 6)
        True
        >>> Fraction(1, 2) < Fraction(1, 2)
        False
        """
        if self.denominator == other.denominator:
            if self.numerator < other.numerator:
                return True
            else:
                return False
        else:
            new_frac_1_num = self.numerator * other.denominator
            new_frac_2_num = self.denominator * other.numerator

            if new_frac_1_num < new_frac_2_num:
                return True
            else:
                return False
    
    def __le__(self, other):
        """Overrides <= operator for Fraction class
        >>> Fraction(3, 2) <= Fraction(20, 4)
        True
        >>> Fraction(3, 2) <= Fraction(3, 2)
        True
        >>> Fraction(5, 2) <= Fraction(1, 2)
        False
        """
        if self < other or self == other:
            return True
        else:
            return False
    
    def __gt__(self, other):
        """Overrides > operator for Fraction class
        >>> Fraction(5, 6) > Fraction(1, 20)
        True
        >>> Fraction(5, 2) > Fraction(56, 3)
        False
        >>> Fraction(1, 9) > Fraction(1, 9)
        False
        """
        if not self < other and not self == other:
            return True
        else:
            return False

    def __ge__(self, other):
        """Overrides >= operator for Fraction class
        >>> Fraction(2, 6) >= Fraction(1, 3)
        True
        >>> Fraction(1, 3) >= Fraction(1, 2)
        False
        >>> Fraction(1, 4) >= Fraction(1, 4)
        True
        """
        if not self < other:
            return True
        else:
            return False

    def __ne__(self, other):
        """Overrides != operator for Fraction class
        >>> Fraction(1, 3) != Fraction(1, 3)
        False
        >>> Fraction(1, 2) != Fraction(5, 6)
        True
        >>> Fraction(3, 2) != Fraction(6, 4)
        False
        """
        if not self == other:
            return True
        else:
            return False
    
    def __sub__(self, other):
        """Overrides - operator for Fraction class
        >>> Fraction(1, 2) - Fraction(1, 2)
        Fraction(0)
        >>> Fraction(3, 2) - Fraction(1, 2)
        Fraction(1)
        >>> Fraction(5, 6) - Fraction(2, 3)
        Fraction(1, 6)
        >>> Fraction(8, 6) - Fraction(2, 3)
        Fraction(2, 3)
        """
        ans_den = self.denominator * other.denominator
        ans_num = (self.numerator * other.denominator) - (self.denominator * other.numerator)

        return Fraction(ans_num, ans_den)
    
    def __mul__(self, other):
        """Overrides * operator for Fraction class
        >>> Fraction(6, 5) * Fraction(1, 2)
        Fraction(3, 5)
        >>> Fraction(1, 2) * Fraction(1, 2)
        Fraction(1, 4)
        >>> Fraction(1, 8) * Fraction(2, 5)
        Fraction(1, 20)
        """
        ans_den = self.denominator * other.denominator
        ans_num = self.numerator * other.numerator

        return Fraction(ans_num, ans_den)
    
    def __truediv__(self, other):
        """Overrides / operator for Fraction class
        >>> Fraction(1, 3) / Fraction(5, 6)
        Fraction(2, 5)
        >>> Fraction(9, 8) / Fraction(4, 5)
        Fraction(45, 32)
        >>> Fraction(1, 9) / Fraction(8, 2)
        Fraction(1, 36)
        """
        ans_num = self.numerator * other.denominator
        ans_den = self.denominator * other.numerator

        return Fraction(ans_num, ans_den)

if __name__ == '__main__':
    import doctest
    doctest.testmod()