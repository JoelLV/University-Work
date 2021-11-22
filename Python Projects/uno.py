import random

class UnoCard:
    def __init__(self, color, rank):
        """Creates a Uno Card object given color and rank in String
        >>> card = UnoCard("R", "8")
        >>> card.color
        'R'
        >>> card.rank
        '8'
        >>> card = UnoCard("G", "D")
        >>> card.color
        'G'
        >>> card.rank
        'D'
        """
        self.color = color
        self.rank = rank
    
    def __str__(self):
        """Returns a string representing the object UnoCard
        >>> str(UnoCard("R", "8"))
        'R8'
        >>> str(UnoCard("K", "W"))
        'KW'
        >>> str(UnoCard("B", "R"))
        'BR'
        """
        return self.color + self.rank
    
    def __repr__(self):
        """Python code that represents the object UnoCard
        >>> UnoCard("Y", "D")
        UnoCard('Y', 'D')
        >>> UnoCard("8", "S")
        UnoCard('8', 'S')
        >>> UnoCard("K", "F")
        UnoCard('K', 'F')
        """
        return f"UnoCard('{self.color}', '{self.rank}')"
    
    def __add__(self, other):
        """Returns the total score of two Uno Cards
        >>> UnoCard("Y", "R") + UnoCard("G", "2")
        22
        >>> UnoCard("R", "S") + UnoCard("K", "F")
        70
        >>> UnoCard("K", "W") + UnoCard("Y", "0")
        50
        >>> UnoCard("Y", "1") + 2
        3
        """
        if isinstance(other, int):
            return other + self.score_value()
        else:
            return self.score_value() + other.score_value()
    
    def can_be_played_on(self, other):
        """Determines whether self can be played on other
        >>> UnoCard("K", "F").can_be_played_on(UnoCard("Y", "8"))
        True
        >>> UnoCard("Y", "4").can_be_played_on(UnoCard("Y", "R"))
        True
        >>> UnoCard("G", "D").can_be_played_on(UnoCard("Y", "2"))
        False
        >>> UnoCard("B", "7").can_be_played_on(UnoCard("R", "7"))
        True
        >>> UnoCard("G", "5").can_be_played_on(UnoCard("R", "2"))
        False
        """
        if self.color == 'K':
            return True
        elif self.color == other.color:
            return True
        elif self.rank == other.rank:
            return True
        else:
            return False
    
    def score_value(self):
        """Determines value of a card according to rank
        >>> UnoCard("B", "7").score_value()
        7
        >>> UnoCard("R", "9").score_value()
        9
        >>> UnoCard("Y", "S").score_value()
        20
        >>> UnoCard("G", "D").score_value()
        20
        >>> UnoCard("R", "R").score_value()
        20
        >>> UnoCard("K", "W").score_value()
        50
        >>> UnoCard("K", "F").score_value()
        50
        """
        if self.color == 'K':
            return 50
        else:
            if self.rank.isnumeric():
                return int(self.rank)
            else:
                return 20

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
    shuffled_deck = deck.copy()
    for index in range(len(shuffled_deck)):
        index_to_switch = random.randint(0, len(shuffled_deck) - 1)
        temp_elem = shuffled_deck[index]
        shuffled_deck[index] = shuffled_deck[index_to_switch]
        shuffled_deck[index_to_switch] = temp_elem
    
    return shuffled_deck

def all_card_colors():
    """Returns a list containing all possible colors in a Uno Deck
    >>> colors = all_card_colors()
    >>> len(colors)
    5
    >>> "R" in colors
    True
    >>> "G" in colors
    True
    >>> "B" in colors
    True
    >>> "Y" in colors
    True
    >>> "K" in colors
    True
    """
    return ["R", "G", "B", "Y", "K"]

def all_card_ranks():
    """Returns a list containing all possible ranks in a Uno Deck
    >>> ranks = all_card_ranks()
    >>> len(ranks)
    15
    >>> '2' in ranks
    True
    >>> '5' in ranks
    True
    >>> '0' in ranks
    True
    >>> '9' in ranks
    True
    >>> '7' in ranks
    True
    >>> 'S' in ranks
    True
    >>> 'D' in ranks
    True
    >>> 'R' in ranks
    True
    >>> 'W' in ranks
    True
    >>> 'F' in ranks
    True
    """
    return ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "S", "D", "R", "W", "F"]

def create_deck():
    """Creates and returns a shuffled list containing all the Uno Cards (108 total)
    >>> deck = create_deck()
    >>> len(deck)
    108
    >>> deck = [str(elem) for elem in deck]
    >>> len(set(deck))
    54
    """
    deck = []
    color_list = all_card_colors()
    rank_list = all_card_ranks()

    for color in color_list[:len(color_list) - 1]:
        deck.append(UnoCard(color, rank_list[0]))
        for rank in rank_list[1:13]:
            deck.append(UnoCard(color, rank))
            deck.append(UnoCard(color, rank))
    for rank in rank_list[-2:]:
        for _ in range(4):
            deck.append(UnoCard(color_list[-1], rank))

    deck = shuffle_deck(deck)

    return deck

def deal_hands(deck, num_hands):
    """Returns a tuple of num_hands lists of 7 cards dealt from deck, 1
    to each hand at a time. Removes the cards that were dealt from the
    'top' of the deck.
    >>> deck = create_deck()
    >>> cards_to_distribute = deck[:14]
    >>> cards_for_players = deal_hands(deck, 2)
    >>> cards_for_players[0][0] == cards_to_distribute[0]
    True
    >>> cards_for_players[1][0] == cards_to_distribute[1]
    True
    >>> len(cards_for_players[0])
    7
    >>> len(cards_for_players)
    2
    >>> len(deck)
    94
    """
    all_hands = []
    
    for hand in range(num_hands):
        all_hands.append([])
    for _ in range(7):
        for hand in all_hands:
            hand.append(deck[0])
            deck.pop(0)
    return tuple(all_hands)

def hand_score(hand):
    """Returns total score of given hand
    >>> hand_score([UnoCard("G", "7"), UnoCard("G", "R")])
    27
    >>> hand_score([UnoCard("K", "W"), UnoCard("K", "F")])
    100
    >>> hand_score([UnoCard("R", "D"), UnoCard("B", "S")])
    40
    >>> hand_score([UnoCard("Y", "1"), UnoCard("R", "2")])
    3
    >>> hand_score([UnoCard("K", "W"), UnoCard("G", "0")])
    50
    """
    total_score = 0

    for card in hand:
        total_score = card + total_score
    
    return total_score
if __name__ == '__main__':
    import doctest
    doctest.testmod()