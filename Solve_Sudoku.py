#!/usr/bin/python3

from CheckSudoku import CheckSudokuCase
import numpy as np

Sudoku1 = np.loadtxt('shudu.txt', dtype=int)


def SolveSudoku(Shudu):
    i, j = start_point(Shudu)
    if i>=8 and j>=8 and Shudu[i][j]!=0:
        return True
    for value in range(1,10):
        Shudu[i][j] = value
        Valid = CheckSudokuCase(Shudu)
        if Valid:
            Shudu[i][j] = value 
            if not SolveSudoku(Sudoku1):
                Shudu[i][j] = 0 
            else:
                return True
        else:
            Shudu[i][j] = 0
    return False



def start_point(Shudu):
    for i in range(9):
        for j in range(9):
            if not Shudu[i][j]:
                return i, j
    return i, j


if __name__ == '__main__':
    ans = SolveSudoku(Sudoku1)
    print(ans)
    print(Sudoku1)
