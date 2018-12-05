#!/usr/bin/python3

def CheckSudokuCase(SudokuCase):
    s = set()

    for i in range(9):
        for j in range(9):
            if SudokuCase[i][j] == 0:
                SudokuCase[i][j] = 0
            elif SudokuCase[i][j] in s:
                return False
            else:
                s.add(SudokuCase[i][j])
        s.clear()

        for k in range(9):
            if SudokuCase[k][i] == 0:
                SudokuCase[k][i] = 0
            elif SudokuCase[k][i] in s:
                return False
            else:
                s.add(SudokuCase[k][i])
        s.clear()

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(i, i + 3):
                for p in range(j, j + 3):
                    if SudokuCase[k][p] == 0:
                        SudokuCase[k][p] = 0
                    elif SudokuCase[k][p] in s:
                        return False
                    else:
                        s.add(SudokuCase[k][p])
                s.clear()

    return True

