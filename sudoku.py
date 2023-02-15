# pylint: disable=missing-docstring

import sys
import random

t_grid = [
    [7,0,0,  0,0,9,  0,0,0],
    [0,0,0,  6,0,0,  0,4,0],
    [0,0,2,  0,0,0,  0,0,0],

    [0,0,0,  0,0,0,  4,0,0],
    [0,5,0,  0,4,6,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],

    [0,0,6,  0,0,0,  0,0,5],
    [2,0,0,  5,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,3,0]
]





def sudoku_solver(grid):
    new_grid = []

    #creating list without nulls:
    for r in range(0,9):
        n_nulls = [x for x in grid[r] if x != 0]

    # creating negativ list of nun_nulls:
        compl = list(range(1,10))
        for nn in n_nulls:
            compl.remove(nn)

    # creating new_row, replacing non_nulls by random.choice of negative list:
        new_line = []
        for x in grid[r]:
            if x != 0:
                new_line.append(x)
            else:
                z = random.choice(compl)
                new_line.append(z)
                compl.remove(z)
        new_grid.append(new_line)
    return new_grid


if __name__ == '__main__':
    print(sudoku_solver(t_grid))
