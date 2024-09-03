import numpy as np
import time


def is_valid(sudoku, x, y, value):
    return (
        value not in sudoku[x, :]
        and value not in sudoku[:, y]
        and value not in quadrant(sudoku, x, y)
    )


def quadrant(sudoku, x, y):
    xx = x // 3
    yy = y // 3
    return sudoku[xx * 3 : (xx + 1) * 3, yy * 3 : (yy + 1) * 3]


def possibilities(sudoku, x, y):
    possibilities = list()
    for value in range(1, 10):
        if is_valid(sudoku, x, y, value):
            possibilities.append(value)
    return possibilities


def solver(sudoku, solutions):
    for (x, y), value in np.ndenumerate(sudoku):
        if value == 0:
            for possibility in possibilities(sudoku, x, y):
                sudoku[x, y] = possibility
                solver(sudoku, solutions)
                sudoku[x, y] = 0
            return
    solutions.append(sudoku.copy())


def jogar():
    tic = time.perf_counter()
    sudoku = np.array(
        [
            4, 0, 0, 0, 0, 6, 8, 0, 0,
            2, 0, 0, 8, 0, 0, 0, 0, 9,
            9, 0, 1, 0, 0, 3, 0, 5, 6,
            0, 0, 9, 6, 8, 0, 0, 0, 2,
            0, 1, 0, 0, 0, 0, 5, 9, 0,
            0, 0, 8, 0, 0, 9, 7, 0, 0,
            0, 2, 4, 0, 9, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 4, 0, 0,
            0, 0, 7, 3, 0, 0, 0, 0, 0,
        ]
    ).reshape([9, 9])
    solutions = list()
    solver(sudoku, solutions)
    for solution in solutions:
        print(solution)
    toc = time.perf_counter()
    print(f"Sudoku solved in {toc - tic:0.4f} seconds")
