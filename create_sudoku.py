from Sudoku_Seed import Seed_Sudoku
import numpy as np
import random
import time


class CreateMySudoku():
    def __init__(self, count):
        a = random.randint(0,9)
        with open('sudoku.txt', 'a+') as sudoku_file:
            sudoku_file.truncate(0)
            for i in range(count):
                Root_shudu = Seed_Sudoku(a)
                self.Generate_Sudoku(Root_shudu)
                np.savetxt(sudoku_file, Root_shudu, fmt="%d")
                sudoku_file.write('\n')
                


    def Data_Exchange(self, Shudu):
        NumOfExchange = 1
        while(NumOfExchange<20):
            a = random.randint(2,9)
            if a == 9:
                for i in range(9):
                    for j in range(9):
                        if Shudu[i][j] == a:
                            Shudu[i][j] = 2
                        elif Shudu[i][j] == 2:
                            Shudu[i][j] = 9
            else :
                for i in range(9):
                    for j in range(9):
                        if Shudu[i][j] == a:
                            Shudu[i][j] = a+1
                        elif Shudu[i][j] == a+1:
                            Shudu[i][j] = a
            NumOfExchange += 1
        return Shudu
                

    def RowColumn_Exchange(self, Shudu):
        NumOfExchange = 1
        while(NumOfExchange<20):
            Row_a = random.randint(1,8)
            if (Row_a%3) == 2:
                Shudu[[Row_a,Row_a-1], :] = Shudu[[Row_a-1,Row_a], :]
            else:
                Shudu[[Row_a,Row_a+1], :] = Shudu[[Row_a+1,Row_a], :]
            
            Shudu = Shudu.T
            NumOfExchange += 1
        return Shudu



    def Generate_Sudoku(self, Root_shudu):
        self.Data_Exchange(Root_shudu)
        self.RowColumn_Exchange(Root_shudu)
        