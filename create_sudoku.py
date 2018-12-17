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
    def __init__(self, count):
        """ Initializes the generated file and calls the generation function """
        with open('sudoku.txt', 'a+') as sudoku_file:
            sudoku_file.truncate(0)
            # for _ in range(count):
                # random_num = random.randint(0, 9)
                # root_shudu = Seed_Sudoku(random_num)
        self.count_need = count
        self.generate_sudoku()
                # np.savetxt(sudoku_file, self.root_shudu, fmt="%d")
                # sudoku_file.write('\n')


    def change_root(self):
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


    def num_pos(self):
        num_position = []
        for i in range(8):
            num_position.append(set())
        for i in range(9):
            for j in range(9):
                if self.root_shudu[i][j] != 1:
                    num_position[self.root_shudu[i][j]-2].add((i,j))
        # for i in range(8):
        #     print(num_position[i])
        return num_position


    def data_exchange(self, num_position, n):
        tempshudu = self.root_shudu.copy()
        for i in range(8):
            for (row, col) in num_position[i]:
                tempshudu[row][col] = n[i]
        return tempshudu

    
    def perm(self, num_position):
        """ Data transformation"""
        # numofexchange = 1
        n =[2, 3, 4, 5, 6, 7, 8, 9]
        tempcount = 40320
        tempshudu = self.root_shudu.copy()
        with open('sudoku.txt', 'a+') as sudoku_file:
            while tempcount > 0 and self.count_need > 0:
                tail = 7
                j = 7  
                tempshudu = self.data_exchange(num_position, n)
                np.savetxt(sudoku_file, tempshudu, fmt="%d")
                sudoku_file.write('\n')
                tempcount -= 1
                self.count_need -= 1
                if tempcount == 0 or self.count_need == 0:
                            break
                while j >= 1:
                    i = j - 1
                    if n[i] < n [j] :
                        jj = tail
                        k = i + 1
                        while jj > i:
                            if n[jj] > n[i] and n[jj] < n[k]:
                                k = jj
                            jj -= 1
                        n[i],n[k] = n[k],n[i]
                        if len(n) > j:
                            i = j
                            jj = tail
                            while i < jj:
                                n[i],n[jj] = n[jj],n[i]
                                i += 1
                                jj -= 1
                        j = tail
                        
                        tempshudu = self.data_exchange(num_position, n)
                        np.savetxt(sudoku_file, tempshudu, fmt="%d")
                        sudoku_file.write('\n')
                        tempcount -= 1
                        self.count_need -= 1
                        if tempcount == 0 or self.count_need == 0:
                            break
                    else :
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
                self.root_shudu[[rownum, rownum-1], :] = self.root_shudu[[rownum-1, rownum], :]
            else:
                self.root_shudu[[rownum, rownum+1], :] = self.root_shudu[[rownum+1, rownum], :]
            self.root_shudu = self.root_shudu.T
            numofexchange += 1
        return self.root_shudu

    def generate_sudoku(self):
        """ Generate a certain number of sudoku endings"""
        num_position = self.num_pos()
        while self.count_need > 0:
            self.change_root()
            self.rowcolumn_exchange(4)
            num_position = self.num_pos()
            self.count_need = self.perm(num_position)