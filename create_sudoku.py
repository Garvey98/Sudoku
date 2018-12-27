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
    count_need = 0
    s = []
    num_position = []

    def __init__(self, count):
        """ Initializes the generated file and calls the generation function """
        with open('sudoku.txt', 'a+') as sudoku_file:
            sudoku_file.truncate(0)
        self.count_need = count
        self.generate_sudoku()

    def data_exchange(self, shudu, n_num):
        """ Data transformation"""
        for i in range(8):
            for (row, col) in self.num_position[i]:
                if shudu[row][col] == n_num[i]:
                    break
                shudu[row][col] = n_num[i]
        return shudu

    def change_root(self):
        """ Change sudoku map"""
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

    def num_pos(self):
        """ Find the same number position"""
        self.num_position = []
        for i in range(8):
            self.num_position.append(set())
        for i in range(9):
            for j in range(9):
                if self.root_shudu[i][j] != 1:
                    self.num_position[self.root_shudu[i][j]-2].add((i, j))
        # return self.num_position

    def perm(self):
        """ Full Permutation"""
        n_num = [2, 3, 4, 5, 6, 7, 8, 9]
        tempcount = 40320
        tempshudu = []
        for row in range(9):
            tempshudu.append(self.root_shudu[row])
        while tempcount > 0 and self.count_need > 0:
            tail = 7
            j = 7
            tempshudu = self.data_exchange(tempshudu, n_num)
            for row in range(9):
                self.s.append(tempshudu[row].tolist())
            tempcount -= 1
            self.count_need -= 1
            if tempcount == 0 or self.count_need == 0:
                break
            while j >= 1:
                i = j - 1
                if n_num[i] < n_num[j]:
                    temp_j = tail
                    k = i + 1
                    while temp_j > i:
                        if n_num[temp_j] > n_num[i] and n_num[temp_j] < n_num[k]:
                            k = temp_j
                        temp_j -= 1
                    n_num[i], n_num[k] = n_num[k], n_num[i]
                    if len(n_num) > j:
                        i = j
                        temp_j = tail
                        while i < temp_j:
                            n_num[i], n_num[temp_j] = n_num[temp_j], n_num[i]
                            i += 1
                            temp_j -= 1
                    j = tail
                    tempshudu = self.data_exchange(tempshudu, n_num)
                    for row in range(9):
                        self.s.append(tempshudu[row].tolist())
                    tempcount -= 1
                    self.count_need -= 1
                    if tempcount == 0 or self.count_need == 0:
                        break
                else:
                    j -= 1
        return self.count_need

    def rowcolumn_exchange(self, change_num):
        """ Row and column transformation"""
        numofexchange = 1
        temp_list = [1, 2, 3, 4, 5, 6, 7, 8]
        while numofexchange < change_num:
            random.shuffle(temp_list)
            rownum = temp_list[1]
            if (rownum % 3) == 2:
                self.root_shudu[[rownum, rownum-1],
                                :] = self.root_shudu[[rownum-1, rownum], :]
            else:
                self.root_shudu[[rownum, rownum+1],
                                :] = self.root_shudu[[rownum+1, rownum], :]
            self.root_shudu = self.root_shudu.T
            numofexchange += 1
        return self.root_shudu

    def generate_sudoku(self):
        """ Generate a certain number of sudoku endings"""
        while self.count_need > 0:
            self.change_root()
            self.rowcolumn_exchange(4)
            self.num_pos()
            self.count_need = self.perm()
        rowcount = 0
        with open('sudoku.txt', 'a+') as sudoku_file:
            for row in self.s:
                rowtxt = '{} {} {} {} {} {} {} {} {}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                sudoku_file.write(rowtxt)
                sudoku_file.write('\n')
                rowcount += 1
                if rowcount % 9 == 0:
                    sudoku_file.write('\n')
