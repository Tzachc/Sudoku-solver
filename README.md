# Sudoku Solver!

This program read sudoku boards from txt file and solve it using backtracking.

### Methods:
* InRowNumber: check if the number we want to put in is appear in the row.
* InColNumber: check if the number we want to put in is appear in the column.
* localBoxCheck: check if the number is appear in the 3x3 box.
* validPlace: use the 3 methods above to check if we have valid number to place.
* printBoard: pretty print to the board.
* solve_sudoku: main algorithm to solve the board.
* draw: display.

### Input Example:
![alt text](https://github.com/Tzachc/Sudoku-solver/blob/main/data/example_input.png)

### Output Example:
![alt text](https://github.com/Tzachc/Sudoku-solver/blob/main/data/solve.png)

***Draw***

![alt text](https://github.com/Tzachc/Sudoku-solver/blob/main/data/draw.png)


