#!/usr/bin/python3

import numpy as np

# SudokuCase = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
#                        [4, 5, 6, 7, 8, 9, 1, 2, 3],
#                        [7, 8, 9, 1, 2, 3, 4, 5, 6],
#                        [2, 1, 4, 3, 6, 5, 8, 9, 7],
#                        [3, 6, 5, 8, 9, 7, 2, 1, 4],
#                        [8, 9, 7, 2, 1, 4, 3, 6, 5],
#                        [5, 3, 1, 6, 4, 2, 9, 7, 8],
#                        [6, 4, 2, 9, 7, 8, 5, 3, 1],
#                        [9, 7, 8, 5, 3, 1, 6, 4, 2]])


def CheckSudokuCase(SudokuCase):
    s = set()

    for i in range(9):
        for j in range(9):
            if SudokuCase[i][j] in s:
                return False
            else:
                s.add(SudokuCase[i][j])
        s.clear()

        for k in range(9):
            if SudokuCase[k][i] in s:
                return False
            else:
                s.add(SudokuCase[k][i])
        s.clear()

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for k in range(i, i + 3):
                for p in range(j, j + 3):
                    if SudokuCase[k][p] in s:
                        return False
                    else:
                        s.add(SudokuCase[k][p])
                s.clear()

    return True


# def main():
#     cc = CheckSudokuCase(SudokuCase)
#     print(cc)


# if __name__ == "__main__":
#     main()
