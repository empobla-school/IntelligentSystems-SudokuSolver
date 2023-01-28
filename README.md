<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Portfolio][moreinfo-shield]][moreinfo-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">Sudoku Solver</h3>

  <p align="center">
    A Sudoku puzzle solver that, with the use of constraint propagation and backtracking search, can solve any Sudoku puzzle, including Arto Inkala’s world’s hardest Sudoku puzzle, in under 1 second.
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#included-files">Included Files</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This repository contains a Sudoku Solver modeled after the algorithms described by Peter Norvig in his article "[Solving Every Sudoku Puzzle](https://norvig.com/sudoku.html)".

The entrypoint at `index.py` uses easy, medium, hard, and evil sudoku problems from [Web Sudoku](https://www.websudoku.com), a website that generates sudoku problems and allows you to solve them. It also uses the World's Hardest Sudoku by finnish mathematician Arto Inkala (2012).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- INCLUDED FILES -->
## Included Files
* `index.py` - Main entrypoint of the program, and cointains functions relevant to solving the Sudoku problems.
* `grids.py` - File that contains functions that return sudoku grid, for easy importing and selection of sudoku grids.
* `setup.py` - Contains functions relevant to setting up the needed structures for the algorithm to be able to solve the Sudoku problems.
* `tests.py` - Contains a function that verifies that the setup was performed correctly.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

The project uses the following dependency. It is necessary to install it before running the script.
* numpy
   ```sh
   pip install numpy
   ```

### Installation
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/empobla/SudokuSolver.git
   ```
2. Run the script
   ```sh
   python index.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The script proceeds to use Peter Norvig's described method and algorithms to solve all of the sudoku problems, generating an output for each sudoku problem. The sudoku problems may be input in the following formats, all as strings:

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

The output generated for any input sudoku will display in the console as follows:

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

This project is property of Emilio Popovits Blake and Hector R.A.D.. All rights are reserved. Modification or redistribution of this code must have _explicit_ consent from either owner.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Emilio Popovits Blake - [Contact](https://emilioppv.com/contact)

Hector R.A.D. - [Github](https://github.com/HectorRAD)

Project Link: [https://github.com/empobla/SudokuSolver](https://github.com/empobla/SudokuSolver)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Solving Every Sudoku Puzzle](https://norvig.com/sudoku.html)
* [Web Sudoku](https://www.websudoku.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/emilio-popovits

[Python]: https://img.shields.io/badge/python-3776ab?style=for-the-badge&logo=python&logoColor=ffdc52
[Python-url]: https://www.python.org/

[moreinfo-url]: https://emilioppv.com/projects#sudoku-solver
[moreinfo-shield]: https://img.shields.io/badge/more%20info-1b1f24?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAApVBMVEUbHyQbHyQbHyRnam2sra+vsbKys7Wsrq+goqQwNDgaHyQaIilbXWGChIZMT1OYmpwYQFoaICYXRF8WUHQZLjwvMzdwcnaztLZ1d3pcX2IaICUXTG0WUHMXS2sXSGcWT3MaKjcpLTFVWFyFh4lTVllvcnWpqqwYOEwZM0QXTW4XTnAaJS8lKS3IycoYPlYaIyt4e36rra60tba5urutr7BQU1cAAAB8HBV3AAAAAnRSTlOR/KrCyFQAAAABYktHRDZHv4jRAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH5wEZCiUZVutNzgAAAGpJREFUCNdjYGBkggNGBmQeiM+EAjC5zCwsrGzsHJwQLhc3ExMPLxMfP5OAIBODkLCIqBi/uASHpJS0jCyDnLyCopIyh4qqmrqGphYDk5Q2WLGOrh63PsgoA0NDI2NDE1PsFqFw0RyJ6gUAuK4HVipJCoQAAAAuelRYdGRhdGU6Y3JlYXRlAAAImTMyMDLWNTDUNTINMTSwMja3MjLVNjCwMjAAAEFRBQlQZi6pAAAALnpUWHRkYXRlOm1vZGlmeQAACJkzMjAy1jUw1DUyDTE0sDI2tzIy1TYwsDIwAABBUQUJeVmGIQAAAABJRU5ErkJggg==