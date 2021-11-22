import random
from enum import Enum

class Fill(Enum):
    EMPTY = 0
    SHADED = 1
    FILLED = 2
    
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Shape(Enum):
    QUAD = 5
    OVAL = 17
    PYRAMID = 234

class SetCard:
    def __init__(self, number, fill, color, shape):
        '''int in [1,3], Fill, Color, Shape -> SetCard
        >>> card = SetCard(10, Fill.EMPTY, Color.RED, Shape.QUAD)
        >>> card.number
        10
        >>> card.fill
        <Fill.EMPTY: 0>
        >>> card.color
        <Color.RED: 1>
        >>> card.shape
        <Shape.QUAD: 5>
        '''
        self.number = number
        self.fill = fill
        self.color = color
        self.shape = shape
    def __str__(self):
        '''Human-readable representation of this card.
        >>> str(SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL))
        '1SBO'
        >>> str(SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD))
        '2ERQ'
        '''
        return str(self.number) + self.fill.name[0] + self.color.name[0] + self.shape.name[0]
    def __repr__(self):
        '''Python code to recreate this card.
        >>> SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> repr(SetCard(2,Fill.EMPTY,Color.RED,Shape.QUAD))
        'SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD)'
        '''
        return f"SetCard({self.number}, Fill.{self.fill.name}, Color.{self.color.name}, Shape.{self.shape.name})"
    def third_card(self, other):
        '''Returns the third card that makes a set with self and other.
        >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD)
        >>> card2 = SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> print(card1.third_card(card2))
        3FGP
        >>> print(card2.third_card(card1))
        3FGP
        >>> card1 = SetCard(1, Fill.EMPTY, Color.RED, Shape.QUAD)
        >>> card2 = SetCard(1, Fill.EMPTY, Color.BLUE, Shape.OVAL)
        >>> print(card1.third_card(card2))
        1EGP
        '''
        card_3 = SetCard(1, Fill.EMPTY, Color.RED, Shape.QUAD)
        for pos in range(len(str(self))):
            char_card_1 = str(self)[pos]
            char_card_2 = str(other)[pos]
            
            if char_card_1 == char_card_2:
                if pos == 0:
                    card_3.number = int(char_card_1)
                elif pos == 1:
                    card_3.fill = self.fill
                elif pos == 2:
                    card_3.color = self.color
                elif pos == 3:
                    card_3.shape = self.shape
            else:
                if pos == 0:
                    temp_list = [1, 2, 3]
                    temp_list.remove(int(char_card_1))
                    temp_list.remove(int(char_card_2))
                    card_3.number = temp_list[0]
                elif pos == 1:
                    temp_list = list(Fill)
                    temp_list.remove(self.fill)
                    temp_list.remove(other.fill)
                    card_3.fill = temp_list[0]
                elif pos == 2:
                    temp_list = list(Color)
                    temp_list.remove(self.color)
                    temp_list.remove(other.color)
                    card_3.color = temp_list[0]
                elif pos == 3:
                    temp_list = list(Shape)
                    temp_list.remove(self.shape)
                    temp_list.remove(other.shape)
                    card_3.shape = temp_list[0]
        return card_3

def shuffle_deck(deck):
    """Shuffles given list
    >>> deck = [1, 2, 3, 4]
    >>> shuffled_deck = shuffle_deck(deck)
    >>> deck == shuffled_deck
    False
    >>> len(shuffle_deck(deck))
    4
    >>> len(set(shuffle_deck(deck)))
    4
    """
    shuffled_deck = list.copy(deck)
    for index in range(len(shuffled_deck)):
        index_to_switch = random.randint(0, len(shuffled_deck) - 1)
        temp_elem = shuffled_deck[index]
        shuffled_deck[index] = shuffled_deck[index_to_switch]
        shuffled_deck[index_to_switch] = temp_elem
    
    return shuffled_deck

def make_deck():
    '''Returns a list containing a complete Set deck with 81 unique cards.
    >>> deck = make_deck()
    >>> len(deck)
    81
    >>> deck = set(deck)
    >>> len(deck)
    81
    '''
    deck = []
    for num in range(1, 4):
        for type_fill in Fill:
            for type_color in Color:
                for type_shape in Shape:
                    card = SetCard(num, type_fill, type_color, type_shape)
                    deck.append(card)
    deck = shuffle_deck(deck)
    return deck

def is_set(card1, card2, card3):
    '''Determines whether the 3 cards make a set.
    (For each of the 4 traits, all 3 cards are either the same, or all 3 are different.)
    >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> card2 = SetCard(1, Fill.SHADED, Color.GREEN, Shape.QUAD)
    >>> card3 = SetCard(3, Fill.FILLED, Color.BLUE, Shape.OVAL)
    >>> is_set(card1, card2, card3)
    True
    >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> card2 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> card3 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> is_set(card1, card2, card3)
    True
    >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> card2 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> card3 = SetCard(1, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> is_set(card1, card2, card3)
    False
    >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> card2 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> card3 = SetCard(2, Fill.FILLED, Color.RED, Shape.PYRAMID)
    >>> is_set(card1, card2, card3)
    False
    >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> card2 = SetCard(2, Fill.EMPTY, Color.GREEN, Shape.PYRAMID)
    >>> card3 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> is_set(card1, card2, card3)
    False
    >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> card2 = SetCard(2, Fill.EMPTY, Color.RED, Shape.OVAL)
    >>> card3 = SetCard(2, Fill.EMPTY, Color.RED, Shape.PYRAMID)
    >>> is_set(card1, card2, card3)
    False
    '''
    card1 = str(card1)
    card2 = str(card2)
    card3 = str(card3)
    LENGTH_OF_CARD = len(card1)
    is_set = True

    for pos in range(LENGTH_OF_CARD):
        if card1[pos] == card2[pos] == card3[pos]:
            continue
        elif card1[pos] != card2[pos] and card1[pos] != card3[pos] and card2[pos] != card3[pos]:
            continue
        else:
            is_set = False
            break
    
    return is_set

if __name__ == '__main__':
    import doctest
    doctest.testmod()