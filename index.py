from setup import *
from tests import testSetup


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