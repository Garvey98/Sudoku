#!/usr/bin/python3
""" This is the module that generates the sudoku endings"""
import random
import numpy as np


class CreateMySudoku():
    """ This is the class that generates the sudoku endings"""
    root_shudu = np.array([[1, 9, 6, 4, 3, 8, 7, 5, 2],
                           [3, 8, 4, 5, 7, 2, 1, 6, 9],
                           [7, 2, 5, 6, 1, 9, 3, 4, 8],
                           [5, 7, 2, 1, 6, 3, 9, 8, 4],
                           [6, 3, 1, 8, 9, 4, 5, 2, 7],
                           [9, 4, 8, 2, 5, 7, 6, 1, 3],
                           [2, 5, 7, 9, 4, 1, 8, 3, 6],
                           [4, 1, 9, 3, 8, 6, 2, 7, 5],
                           [8, 6, 3, 7, 2, 5, 4, 9, 1]])

    def __init__(self, count):
        """ Initializes the generated file and calls the generation function """
        with open('sudoku.txt', 'a+') as sudoku_file:
            sudoku_file.truncate(0)
            for _ in range(count):
                # random_num = random.randint(0, 9)
                # root_shudu = Seed_Sudoku(random_num)
                self.generate_sudoku()
                np.savetxt(sudoku_file, self.root_shudu, fmt="%d")
                sudoku_file.write('\n')

    def data_exchange(self):
        """ Data transformation"""
        numofexchange = 1
        temp_list = [2, 3, 4, 5, 6, 7, 8, 9]
        while numofexchange < 5:
            random.shuffle(temp_list)
            random_num = temp_list[1]
            if random_num == 9:
                for i in range(9):
                    for j in range(9):
                        if self.root_shudu[i][j] == random_num:
                            self.root_shudu[i][j] = 2
                        elif self.root_shudu[i][j] == 2:
                            self.root_shudu[i][j] = 9
            else:
                for i in range(9):
                    for j in range(9):
                        if self.root_shudu[i][j] == random_num:
                            self.root_shudu[i][j] = random_num+1
                        elif self.root_shudu[i][j] == random_num+1:
                            self.root_shudu[i][j] = random_num
            numofexchange += 1
        return self.root_shudu

    def rowcolumn_exchange(self):
        """ Row and column transformation"""
        numofexchange = 1
        temp_list = [1, 2, 3, 4, 5, 6, 7, 8]
        while numofexchange < 5:
            random.shuffle(temp_list)
            rownum = temp_list[1]
            if (rownum % 3) == 2:
                self.root_shudu[[rownum, rownum-1], :] = self.root_shudu[[rownum-1, rownum], :]
            else:
                self.root_shudu[[rownum, rownum+1], :] = self.root_shudu[[rownum+1, rownum], :]
            self.root_shudu = self.root_shudu.T
            numofexchange += 1
        return self.root_shudu

    def generate_sudoku(self):
        """ Generate a certain number of sudoku endings"""
        self.data_exchange()
        self.rowcolumn_exchange()
