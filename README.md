# Sudoku Solver

## Authors
* Emilio Popovits Blake (A01027265)
* Hector R.A.D. ()

## Description
This repository contains a Sudoku Solver modeled after the algorithms described by Peter Norvig in his article "[Solving Every Sudoku Puzzle](https://norvig.com/sudoku.html)".

The entrypoint at `index.py` uses easy, medium, hard, and evil sudoku problems from [Web Sudoku](https://www.websudoku.com), a website that generates sudoku problems and allows you to solve them. It also uses the World's Hardest Sudoku by finnish mathematician Arto Inkala (2012). It proceeds to use Peter Norvig's described method and algorithms to solve all of the sudoku problems, generating an output for each sudoku problem as follows:

```sh
Easy sudoku puzzle:
2 7 1 |9 6 5 |4 8 3
5 4 3 |8 1 7 |6 9 2
9 6 8 |4 3 2 |1 7 5
------+------+------
7 5 2 |6 8 4 |3 1 9
8 3 9 |5 2 1 |7 6 4
6 1 4 |7 9 3 |2 5 8
------+------+------
1 9 6 |3 4 8 |5 2 7
4 2 5 |1 7 9 |8 3 6
3 8 7 |2 5 6 |9 4 1
Solved Easy sudoku puzzle in 1.9994 miliseconds.
```

## Requirements
* Python3

## Input
The sudoku problems may be input in the following formats, all as strings:
```py
"4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"

"""
400000805
030000000
000700000
020000060
000080400
000010000
000603070
500200000
104000000"""

"""
4 . . |. . . |8 . 5 
. 3 . |. . . |. . . 
. . . |7 . . |. . . 
------+------+------
. 2 . |. . . |. 6 . 
. . . |. 8 . |4 . . 
. . . |. 1 . |. . . 
------+------+------
. . . |6 . 3 |. 7 . 
5 . . |2 . . |. . . 
1 . 4 |. . . |. . . 
"""
```

Where `0` and `.` work as placeholders for empty values in the sudoku grid, and all other values which are not from 1-9 are ignored.

## Included Files
* `index.py` - Main entrypoint of the program, and cointains functions relevant to solving the Sudoku problems.
* `grids.py` - File that contains functions that return sudoku grid, for easy importing and selection of sudoku grids.
* `setup.py` - Contains functions relevant to setting up the needed structures for the algorithm to be able to solve the Sudoku problems.
* `tests.py` - Contains a function that verifies that the setup was performed correctly.