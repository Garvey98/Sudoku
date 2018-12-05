#!/usr/bin/python3

from CheckSudoku import CheckSudokuCase
from Sudoku_Seed import Seed_Sudoku
import numpy as np
import random
import time

def Data_Exchange(Shudu):
    NumOfExchange = 1
    while(NumOfExchange<10):
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
            

def RowColumn_Exchange(Shudu):
    NumOfExchange = 1
    while(NumOfExchange<10):
        Row_a = random.randint(1,8)
        if (Row_a%3) == 2:
            Shudu[[Row_a,Row_a-1], :] = Shudu[[Row_a-1,Row_a], :]
        else:
           Shudu[[Row_a,Row_a+1], :] = Shudu[[Row_a+1,Row_a], :]
        
        Shudu = Shudu.T
        NumOfExchange += 1
    return Shudu



if __name__ == '__main__':

    num = input('-c ')
    num = int(num)
    start_time = time.time()
    f = open('sudoku.txt', "r+")
    f.truncate()
    f.close
    a = random.randint(0,9)
    testshudu = Seed_Sudoku(a)

    with open('sudoku.txt', 'a+') as sudoku_file:
        while(num > 0):
            # start_time0 = time.time()
            testshudu = Data_Exchange(testshudu)
            testshudu = RowColumn_Exchange(testshudu)
            # print("[TIME]00 ", time.time() - start_time0)
            # print(testshudu)

            # start_time1 = time.time()
            np.savetxt('shudu.txt',testshudu, fmt="%d")
            sudoku_file.write('\n')
            num -= 1
            # print("[TIME]11 ", time.time() - start_time1)
    

    # while(num>0):
    #     start_time0 = time.time()
    #     testshudu = Data_Exchange(testshudu)
    #     testshudu = RowColumn_Exchange(testshudu)
    #     print("[TIME]00 ", time.time() - start_time0)
    #     # print(testshudu)

    #     start_time1 = time.time()
    #     np.savetxt('shudu.txt',testshudu, fmt="%d")
    #     fp = open('shudu.txt','r')
    #     for line in fp:
    #         fq = open('sudoku.txt','a')#这里用追加模式
    #         fq.write(line)
    #     num -= 1
    #     fq.write('\n')
    #     fp.close()
    #     fq.close()
    #     print("[TIME]11 ", time.time() - start_time1)

    print("[TIME]", time.time() - start_time)