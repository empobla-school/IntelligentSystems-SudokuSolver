import time
from setup import *
from tests import testSetup
from grids import *

def parse_grid(grid : str, digits : str, squares : list[str], peers : dict[str, set]):
    '''
    Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected.
    
    :param str grid: Sudoku grid string representation
    :param str digits: All possible digits for sudoku
    :param list squares: All possible squares in sudoku grid
    :param dict peers: All peers for each square in sudoku grid
    '''
    # To start, every square can be any digit; then assign values from the grid.
    values = dict((square, digits) for square in squares)
    # For each square and digit in the converted grid values dictionary 
    for square, digit in grid_values(grid, digits, squares).items():
        # If digit is a valid digit and 
        if digit in digits and not assign(values, square, digit, peers):
            return False # (Fail if we can't assign d to square s.)
    return values


def grid_values(grid : str, digits : str, squares : list[str]) -> dict[str, str]:
    '''
    Convert grid into a dict of {square: char} with '0' or '.' for empties.
    
    :param str grid: Sudoku grid string representation
    :param str digits: All possible digits for sudoku
    :param list squares: All possible squares in sudoku grid
    '''
    chars = [c for c in grid if c in digits or c in '0.']
    # Make sure that there are 81 characters
    assert len(chars) == 81
    # Return a dictionary of squares with each character
    return dict(zip(squares, chars))


def assign(values : dict[str, str], square : str, digit : str, peers : dict[str, set]):
    '''
    Eliminate all the other values (except digit) from values[square] and propagate.
    Return values, except return False if a contradiction is detected.
    
    :param dict values: All possible values for all possible squares in a sudoku grid
    :param str square: Square in sudoku grid to assign digit to
    :param str digit: Digit to assign and propagate to a sudoku square
    :param dict peers: All peers for each square in sudoku grid
    '''
    # Get all values for a square without the digit
    other_values = values[square].replace(digit, '')
    if all(eliminate(values, square, digit, peers) for digit in other_values):
        return values
    else:
        return False


def eliminate(values : dict[str, str], square : str, digit : str, peers : dict[str, set]):
    '''
    Eliminate digit from values[square]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected.
    
    :param dict values: All possible values for all possible squares in a sudoku grid
    :param str square: Square in sudoku grid to remove digit from
    :param str digit: Digit to remove and propagate from a sudoku square
    :param dict peers: All peers for each square in sudoku grid
    '''
    # If digit is not in the possible values for the square, return the values (digit has already been eliminated)
    if digit not in values[square]:
        return values # Already eliminated
    # Remove digit from square values
    values[square] = values[square].replace(digit,'')
    # (1) If a square is reduced to one value digit, then eliminate digit from the peers.
    if len(values[square]) == 0:
        return False # Contradiction: removed last value
    elif len(values[square]) == 1:
        digit2 = values[square]
        if not all(eliminate(values, square2, digit2, peers) for square2 in peers[square]):
            return False
    # (2) If a unit is reduced to only one place for a value digit, then put it there.
    for unit in units[square]:
        # Possible places for a digit in a unit
        dplaces = [square for square in unit if digit in values[square]]
        if len(dplaces) == 0:
            return False # Contradiction: no place for this value
        elif len(dplaces) == 1:
            # digit can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], digit, peers):
                return False
    return values


def display(values : dict[str, str], name: str, time : float) -> None:
    '''
    Display sudoku square possible values as a 2-D grid.
    
    :param dict values: All possible values for all possible squares in a sudoku grid
    :param str name: Sudoku puzzle name
    :param float time: Time taken to solve puzzle
    '''
    print(f'{name} sudoku puzzle:')
    width = 1 + max(len(values[square]) for square in squares)
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in rows:
        print(''.join(values[row + col].center(width) + ('|' if col in '36' else '') for col in cols))
        if row in 'CF': print(line)
    print(f'Solved {name} sudoku puzzle in {round(time, 4)} miliseconds.')
    print()


def solve(grid : str, digits : str, squares : list[str], peers : dict[str, set]): 
    '''Solves sudoku grid by using DFS and propagation'''
    return search(parse_grid(grid, digits, squares, peers), peers)


def search(values : dict[str, str], peers : dict[str, set]):
    '''Using depth-first search and propagation, try all possible values.'''
    # If search failed earlier, return false as to say that this solution failed
    if values is False:
        return False # Failed earlier
    
    # If all squares only have 1 value, sudoku grid has been solved
    if all(len(values[square]) == 1 for square in squares): 
        return values # Solved!
    
    # Chose the unfilled square with the fewest possibilities
    n, square = min((len(values[square]), square) for square in squares if len(values[square]) > 1)
    return some(search(assign(values.copy(), square, digit, peers), peers) for digit in values[square])


def some(seq):
    '''Return some element of seq that is true.'''
    for e in seq:
        if e: return e
    return False


if __name__ == "__main__":
    numbers = '123456789'
    rows = 'ABCDEFGHI'
    cols = numbers

    # Get all possible sudoku squares
    squares = getAllSquares(rows, cols)
    # Get all possible units
    unitlist = getAllUnits(rows, cols)
    # Map all units to their squares
    units = getSquareUnitsMap(unitlist, squares)
    # Get all square peers
    peers = getAllSquarePeers(units, squares)

    # Test that squares, unitlist, units, and peers were formed correctly
    testSetup(squares, unitlist, units, peers)

    # Easy sudoku
    easy_sudoku = getEasy()
    easy_start = time.time()
    easy_solution = solve(easy_sudoku, numbers, squares, peers)
    easy_end = time.time()
    easy_time = (easy_end - easy_start) * 1000
    display(easy_solution, 'Easy', easy_time)

    # Medium sudoku
    medium_sudoku = getMedium()
    medium_start = time.time()
    medium_solution = solve(medium_sudoku, numbers, squares, peers)
    medium_end = time.time()
    medium_time = (medium_end - medium_start) * 1000
    display(medium_solution, 'Medium', medium_time)
    
    # Hard sudoku
    hard_sudoku = getHard()
    hard_start = time.time()
    hard_solution = solve(hard_sudoku, numbers, squares, peers)
    hard_end = time.time()
    hard_time = (hard_end - hard_start) * 1000
    display(hard_solution, 'Hard', hard_time)
    
    # Evil sudoku
    evil_sudoku = getHard()
    evil_start = time.time()
    evil_solution = solve(evil_sudoku, numbers, squares, peers)
    evil_end = time.time()
    evil_time = (evil_end - evil_start) * 1000
    display(evil_solution, 'Evil', evil_time)
    
    # World's Hardest sudoku
    worldhardest_sudoku = getHard()
    worldhardest_start = time.time()
    worldhardest_solution = solve(worldhardest_sudoku, numbers, squares, peers)
    worldhardest_end = time.time()
    worldhardest_time = worldhardest_end - worldhardest_start
    display(worldhardest_solution, 'World\'s Hardest', worldhardest_time)

    # Class sudoku
    class_sudoku = getHard()
    class_start = time.time()
    class_solution = solve(class_sudoku, numbers, squares, peers)
    class_end = time.time()
    class_time = (class_end - class_start) * 1000
    display(class_solution, 'Class', class_time)