def cross(A : list, B : list) -> list:
    ''' Cross product of elements in A and elements in B. '''
    return [ a + b for a in A for b in B ]


def getAllSquares(rows : str, cols: str) -> list:
    ''' Returns list with all possible sudoku squares. '''
    # [A1 A2 A3 A4 A5 A6 A7 A8 A9 B1 ... I7 I8 I9]
    squares = cross(rows, cols)
    # squares = []
    # for letter in rows:
    #     for number in cols:
    #         squares.append(letter + number)
    return squares


def getAllUnits(rows : str, cols: str) -> list:
    ''' Returns list with all possible units (columns, rows, boxes). '''
    # All possible columns
    # [A1 B1 C1 D1 E1 F1 G1 H1 I1], [A2 B2 C2 D2 E2 F2 G2 H2 I2], ...
    unitcols = [ cross(rows, number) for number in cols ]
    # unitcols = []
    # for number in cols:
    #     unitcols.append(cross(rows, number))

    # All possible rows
    # [A1 A2 A3 A4 A5 A6 A7 A8 A9], [B1 B2 B3 B4 B5 B6 B7 B8], ...
    unitrows = [ cross(letter, cols) for letter in rows ]
    # for letter in rows:
    #     unitrows.append(cross(letter, cols))
    
    # All possible boxes
    # [A1 A2 A3 B1 B2 B3 C1 C2 C3], ..., [A7 A7 A9 B7 B8 B9 C7 C8 C9], [D1 D2 D3 E1 E2 E3 F1 F2 F3], ..., [D7 D8 D9 E7 E8 E9 F7 F8 F9], ...
    # (ABC, DEF, GHI), (123, 456, 789)
    unitboxes = [ cross(letterGroup, numberGroup) for letterGroup in ('ABC', 'DEF', 'GHI') for numberGroup in ('123', '456', '789') ]
    # unitboxes = []
    # for letterGroup in ('ABC', 'DEF', 'GHI'):
    #     for numberGroup in ('123', '456', '789'):
    #         unitboxes.append(cross(letterGroup, numberGroup))

    unitlist = ( unitcols + unitrows + unitboxes )
    return unitlist


def getSquareUnitsMap(unitlist : list, squares : list) -> dict:
    '''
    Returns all units mapped to individual squares (square: [column, row, box]). 
    
    :param list unitlist: List with all possible units
    :param list squares: List with all sudoku squares
    '''
    # {A1: [col that contains A1, row that contains A1, box that contains A1]}, {B2: ...}, ...
    units = dict((square, [ item for item in unitlist if square in item ]) for square in squares)
    # units = dict()
    # for square in squares:
    #     squareunits = []
    #     for item in unitlist:
    #         if square in item:
    #             squareunits.append(item)
    #     units[square] = squareunits
    return units


def getAllSquarePeers(units : dict, squares : list) -> dict:
    '''
    Returns all squares' peers.
    
    :param dict units: All squares' units
    :param list squares: List with all sudoku squares
    '''
    # Peers are all units on which a square appears
    # A1 appears on its row, its column, and its box. Get all squares in each of those lists
    # {A1:{B3 A4 A6 C3 E1 F1 A8 A7 A2 G1 I1 A3 B1 A9 C1 D1 H1 C2 B2 A5}, {A2: ...}, ...
    peers = dict((square, set(sum(units[square], [])) - set([square])) for square in squares)
    # peers = dict()
    # for square in squares:
    #     squarepeers = set(sum(units[square], [])) - set([square])
    #     peers[square] = squarepeers
    return peers