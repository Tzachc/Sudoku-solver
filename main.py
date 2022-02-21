'''
This program can solve sudoku game using recursion and backtracking.
Using pygame to display the finish board.
'''
import pygame

GRID_SIZE = 9


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 20
HEIGHT = 20
MARGIN = 5
pygame.init()

WINDOW_SIZE = [235, 235]
screen = pygame.display.set_mode(WINDOW_SIZE)

screen.fill(WHITE)
pygame.display.set_caption('Sudoku solver!')

def draw(grid, isdone):

    done = False

    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont("monospace", 20)

    while not done:
        # Draw the grid
        for row in range(9):
            for column in range(9):
                color = WHITE

                if grid[row][column] == 0:
                    color = WHITE

                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                label = myfont.render(str(grid[row][column]), 1, BLACK)
                screen.blit(label, [(MARGIN + WIDTH) * column + MARGIN+5, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                pygame.draw.line(screen, BLACK, [77, 0], [77, 250], 2)
                pygame.draw.line(screen, BLACK, [152, 0], [152, 250], 2)

                pygame.draw.line(screen, BLACK, [0, 77], [250, 77], 2)
                pygame.draw.line(screen, BLACK, [0, 151], [250, 151], 2)

        clock.tick(60)

        pygame.display.flip()

        if(not isdone):
            done = True



def InRowNumber(board, numberToCheck, row):
    for i in range(GRID_SIZE):
        if board[row][i] == str(numberToCheck):
            return True
    return False

def InColNumber(board,numberToCheck,col):
    for i in range(GRID_SIZE):
        if board[i][col] == str(numberToCheck):
            return True
    return False

def localBoxCheck(board,numberToCheck,row,col):
    localRow = row - row%3
    localCol = col - col%3
    for i in range(localRow,localRow+3):
        for j in range(localCol,localCol+3):
            temp_num = board[i][j]
            if temp_num == str(numberToCheck):

                return True
    return False
'''
Main algorithm, backtracking.
Trying to put every number between 1-9 and see if it valid.
if it does, we keep going, if not, we going back and delete the last
number we put, and trying the next number.
'''
def solve_sudoku(board):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == str(0):
                for numberToTry in range(1,GRID_SIZE+1):
                    if validPlace(board,numberToTry,i,j):
                        board[i][j] = str(numberToTry)
                        if solve_sudoku(board):
                            return True
                        else:
                            board[i][j] = '0'
                return False
    return True

def validPlace(board,numberToPut,row,col):
    row_check = InRowNumber(board,numberToPut,row)
    col_check = InColNumber(board,numberToPut,col)
    box_check = localBoxCheck(board,numberToPut,row,col)
    if row_check == True or col_check == True or box_check == True:
        return False
    return True

def print_board(board):
    for i,row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("---------------------")
        for j,col in enumerate(board):
            if j % 3 == 0 and j != 0:
                print("|", end =" ")
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=" ")
def main():
    with open("Grid.txt") as textFile:
        lines = [line.split() for line in textFile]
        print("Before: ")
        print_board(lines)
        print("\n After: ")
        solve_sudoku(lines)
        print_board(lines)
        draw(lines,True)
if __name__ == "__main__":
    main()