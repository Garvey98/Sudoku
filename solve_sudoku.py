#!/usr/bin/python3
""" This is the module that solves the sudoku"""
import numpy as np

class SolveMySudoku():
    """ This is the class that solves the sudoku"""
    mysudoku = np.zeros((9, 9), dtype=int)
    print(mysudoku)
    def __init__(self, Soduku_Path):
        """ Load the sudoku from the file and call the solution function to output the result"""
        allmysudoku = np.loadtxt(Soduku_Path, dtype=int)
        sudoku_count = int(len(allmysudoku)/9)
        sudoku_now = np.split(allmysudoku, sudoku_count)
        with open('Sudoku_Problem_Answer.txt', 'a+') as sudoku_answer:
            sudoku_answer.truncate(0)
            for mysudoku1 in sudoku_now:
                self.mysudoku = mysudoku1
                self.solve_the_sudoku()
                np.savetxt(sudoku_answer, self.mysudoku, fmt="%d")
                sudoku_answer.write('\n')

    def smallest_possibility_first_dfs(self, blank, row_num, col_num, block_num):
        """ Select the location with the fewest possible values for depth-first search"""
        blank_length = len(blank)
        if blank_length == 0:
            print(self.mysudoku)
            return True

        all_num = set(range(1, 10))
        smallest_possible_case = 9
        for (row, col) in blank:
            possibility = all_num - \
                (row_num[row] | col_num[col] | block_num[row//3][col//3])
            # print(possibility, row, col)
            if len(possibility) <= smallest_possible_case:
                smallest_possible_case = len(possibility)
                i = row
                j = col

        if smallest_possible_case == 0:
            return False

        # print("smallest: ", possibility, row, col)
        blank.remove((i, j))
        possibility = all_num - \
            (row_num[i] | col_num[j] | block_num[i//3][j//3])

        for num in possibility:
            row_num[i].add(num)
            col_num[j].add(num)
            block_num[i//3][j//3].add(num)
            self.mysudoku[i][j] = num
            if self.smallest_possibility_first_dfs(blank, row_num, col_num, block_num):
                return True
            self.mysudoku[i][j] = 0
            row_num[i].remove(num)
            col_num[j].remove(num)
            block_num[i//3][j//3].remove(num)

        blank.add((i, j))
        return False


    def solve_the_sudoku(self):
        """ Analyze rows, columns, and blocks of sudoku"""

        col_num = []
        row_num = []
        block_num = [[0]*3 for i in range(3)]

        for i in range(9):
            col_num.append(set())
            row_num.append(set())

        for i in range(3):
            for j in range(3):
                block_num[i][j] = set()

        blank = set()

        for i in range(9):
            for j in range(9):
                if self.mysudoku[i][j] != 0:
                    if self.mysudoku[i][j] not in row_num[i]:
                        row_num[i].add(self.mysudoku[i][j])
                    if self.mysudoku[i][j] not in col_num[j]:
                        col_num[j].add(self.mysudoku[i][j])
                    if self.mysudoku[i][j] not in block_num[i//3][j//3]:
                        block_num[i//3][j//3].add(self.mysudoku[i][j])
                else:
                    blank.add((i, j))

        self.smallest_possibility_first_dfs(
            blank, row_num, col_num, block_num)
