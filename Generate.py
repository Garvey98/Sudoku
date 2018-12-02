#!/usr/bin/python3

from CheckSudoku import CheckSudokuCase
import numpy as np
import random

testshudu = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [2, 1, 4, 3, 6, 5, 8, 9, 7],
                      [3, 6, 5, 8, 9, 7, 2, 1, 4],
                      [8, 9, 7, 2, 1, 4, 3, 6, 5],
                      [5, 3, 1, 6, 4, 2, 9, 7, 8],
                      [6, 4, 2, 9, 7, 8, 5, 3, 1],
                      [9, 7, 8, 5, 3, 1, 6, 4, 2]])

def Data_Exchange(Shudu):
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
            

def RowColumn_Exchange(Shudu):
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


testshudu = Data_Exchange(testshudu)
# print(testshudu)
testshudu = RowColumn_Exchange(testshudu)
print(testshudu)
# print(testshudu.T)

hh = CheckSudokuCase(testshudu)
print(hh)

# print(testshudu[0])

np.savetxt('shudu.txt',testshudu, fmt="%d")

fp = open('shudu.txt','r')
for line in fp:
    fq = open('sudoku.txt','a')#这里用追加模式
    fq.write(line)
fq.write('\n')
fp.close()
fq.close()