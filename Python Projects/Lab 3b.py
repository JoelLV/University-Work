"""Sliding Puzzle
Prof. O and Joel Lopez Villarreal
2021-09-16 first draft
2021-09-19 final draft

A Sliding Puzzle is represented by a string
whose length is a perfect square
of an integer in [2, 6] (i.e., 4, 9, 16, 25, or 36).
It contains only digits (0-9) and capital letters (A-Z),
exactly ONE of which (typically 0) is "empty"
and is represented by a hyphen (-).

On screen, however, the layout is an NxN square.
Legal moves consist of sliding a tile
up, down, left, or right (but never diagonally)
into the empty spot (-).

The puzzle is in the "solved" state when
all its digits and letters are in ascending order
(with digits before letters, as in ASCII and Unicode)
and the empty spot is at the beginning or end
(never in the middle).

References:
https://mathworld.wolfram.com/15Puzzle.html
https://lorecioni.github.io/fifteen-puzzle-game/
https://15puzzle.netlify.app/
"""

from typing import Tuple
import math

def rows_from_puzzle(puzzle : str) -> None:
    """Returns a string with a newline between rows of the puzzle.
    >>> rows_from_puzzle('123-')
    '12\\n3-'
    >>> rows_from_puzzle('1j3a9s3a-')
    '1j3\\na9s\\n3a-'
    >>> rows_from_puzzle('123456789-abcdef')
    '1234\\n5678\\n9-ab\\ncdef'
    >>> rows_from_puzzle('123-4')
    '12\\n3-\\n4'
    >>> rows_from_puzzle('')
    ''
    """
    break_line = int(math.sqrt(len(puzzle)))
    better_puzzle_str = ''
    num_of_elem_iterated_per_row = 0
    
    for index in range(len(puzzle)):
        better_puzzle_str += puzzle[index]
        num_of_elem_iterated_per_row += 1
        if num_of_elem_iterated_per_row == break_line and index < len(puzzle) - 1:
            better_puzzle_str += "\n"
            num_of_elem_iterated_per_row = 0

    return better_puzzle_str

def is_solved(puzzle : str) -> bool:
    """Determines whether puzzle is solved (as defined above).
    >>> is_solved('123-')
    True
    >>> is_solved('12-3')
    False
    >>> is_solved('132-')
    False
    >>> is_solved('123456789abcdef-')
    True
    >>> is_solved('1af23456789bcde-')
    False
    >>> is_solved('abcdef123456789-')
    False
    >>> is_solved('12345678-')
    True
    >>> is_solved('13456782-')
    False
    >>> is_solved('-123')
    True
    >>> is_solved('-231')
    False
    """
    if puzzle[-1] == '-' or puzzle[0] == '-':
        if puzzle[-1] == '-':
            start_index, end_index = 0, len(puzzle) - 1
        else:
            start_index, end_index = 1, len(puzzle)
        for index in range(start_index, end_index - 1):
            if ord(puzzle[index]) > ord(puzzle[index + 1]):
                return False
        else:
            return True
    else:
        return False 
    

def is_legal_move(puzzle : str, tile_to_move : str) -> bool:
    """Determines whether it is possible to move tile_to_move into the empty spot.
    >>> is_legal_move('123-56789', '5')
    True
    >>> is_legal_move('123456789a-bcdef', 'a')
    True
    >>> is_legal_move('123456789a-bcdef', 'f')
    False
    >>> is_legal_move('12-3', '3')
    True
    >>> is_legal_move('123-56789', '3')
    False
    >>> is_legal_move('123-56789', '1')
    True
    >>> is_legal_move('123456-78', '6')
    False
    >>> is_legal_move('123-56789', '7')
    True
    >>> is_legal_move('1-34', '1')
    True
    >>> is_legal_move('12356-789', '7')
    False
    >>> is_legal_move('7DA1C2FE-468395B', 'C')
    True
    """
    
    ELEMENTS_PER_ROW = int(math.sqrt(len(puzzle)))

    list_of_elements_per_row = []
    num_of_row_for_tile = 0
    num_of_row_for_whitespace = 0
    
    list_of_elements_per_row = [puzzle[index:index + ELEMENTS_PER_ROW] for index in range(0, len(puzzle), ELEMENTS_PER_ROW)]

    if tile_to_move == '-':
        return False
    else:
        for list_index in range(len(list_of_elements_per_row)):
            if tile_to_move in list_of_elements_per_row[list_index]:
                index_of_tile = list_of_elements_per_row[list_index].index(tile_to_move)
                num_of_row_for_tile = list_index
                if '-' in list_of_elements_per_row[list_index]:
                    index_of_white_space = list_of_elements_per_row[list_index].index('-')
                    if index_of_tile - 1 == index_of_white_space or index_of_tile + 1 == index_of_white_space:
                        return True
                    else:
                        return False
                else:
                    break
        for list_index in range(len(list_of_elements_per_row)):
            if '-' in list_of_elements_per_row[list_index]:
                index_of_white_space = list_of_elements_per_row[list_index].index('-')
                num_of_row_for_whitespace = list_index
                if index_of_white_space == index_of_tile and int(abs(num_of_row_for_whitespace - num_of_row_for_tile)) == 1:
                    return True
                else:
                    return False

def puzzle_with_move(puzzle : str, tile_to_move : str) -> str:
    """Move tile_to_move into the empty slot (-).
    >>> puzzle_with_move('123456789a-bcdef', 'a')
    '123456789-abcdef'
    >>> puzzle_with_move('123456789a-bcdef', 'b')
    '123456789ab-cdef'
    >>> puzzle_with_move('1234-56789abcdef', '1')
    '-234156789abcdef'
    >>> puzzle_with_move('1234-56789abcdef', '8')
    '12348567-9abcdef'
    >>> puzzle_with_move('12-4', '2')
    '1-24'
    >>> puzzle_with_move('123-45678', '4')
    '1234-5678'
    >>> puzzle_with_move('123\\n-45\\n678', '1')
    '-23\\n145\\n678'
    """

    changed_puzzle = ''
    index_of_white_space = puzzle.index('-')
    index_of_tile_to_move = puzzle.index(tile_to_move)

    for index in range(len(puzzle)):
        if index == index_of_white_space:
            changed_puzzle += tile_to_move
        elif index == index_of_tile_to_move:
            changed_puzzle += '-'
        else:
            changed_puzzle += puzzle[index]

    return changed_puzzle

def space_puzzle(puzzle : str) -> str:
    return  " " + " ".join(rows_from_puzzle(puzzle))

def play_puzzle(puzzle : str) -> None:
    moves = 0
    while not is_solved(puzzle):
        print(f"\nCurrent puzzle state:\n{space_puzzle(puzzle)}")
        tile_to_move = "-"
        moves += 1
        print(f"Move #{moves}")
        while not is_legal_move(puzzle, tile_to_move):
            tile_to_move = input("Which tile would you like to move into the empty spot? ")        
        puzzle = puzzle_with_move(puzzle, tile_to_move)
    print(f"\nSolved!\n{space_puzzle(puzzle)}")
    print(f"You solved the puzzle in {moves} moves!")

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    play_puzzle('1847295-3')