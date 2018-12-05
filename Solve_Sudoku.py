#!/usr/bin/python3

from CheckSudoku import CheckSudokuCase
import numpy as np
import time

Sudoku1 = np.loadtxt('shudu.txt', dtype=int)
Sudoku2 = np.loadtxt('shudu.txt', dtype=int)


def SolveSudoku(Shudu):
    i, j = start_point(Shudu)
    # print(i,j)
    s = set()
    all_num = set([0,1,2,3,4,5,6,7,8,9])
    if i>=8 and j>=8 and Shudu[i][j]!=0:
        return True
    Count_Block_num(Shudu)
    s = Block_Num_P(Shudu, i, j)
    for value in all_num - s:
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


s_0 = set(); s_1 = set(); s_2 = set(); s_3 = set(); s_4 = set(); s_5 = set(); s_6 = set(); s_7 = set(); s_8 = set()
def Count_Block_num(Shudu):
    s_0.clear(); s_1.clear(); s_2.clear(); s_3.clear(); s_4.clear(); s_5.clear(); s_6.clear(); s_7.clear(); s_8.clear(); 
    for i in range(0,3):
        for j in range(0,3):
            s_0.add(Shudu[i][j])
    for i in range(0,3):
        for j in range(3,6):
            s_1.add(Shudu[i][j])
    for i in range(0,3):
        for j in range(6,9):
            s_2.add(Shudu[i][j])
    for i in range(3,6):
        for j in range(0,3):
            s_3.add(Shudu[i][j])
    for i in range(3,6):
        for j in range(3,6):
            s_4.add(Shudu[i][j])
    for i in range(3,6):
        for j in range(6,9):
            s_5.add(Shudu[i][j])
    for i in range(6,9):
        for j in range(0,3):
            s_6.add(Shudu[i][j])
    for i in range(6,9):
        for j in range(3,6):
            s_7.add(Shudu[i][j])
    for i in range(6,9):
        for j in range(6,9):
            s_8.add(Shudu[i][j])
    


def Block_Num_P(Shudu, r, c):
    if r<3 and c<3:
        return s_0
    if r<3 and 3<=c<6:
        return s_1
    if r<3 and c>=6:
        return s_2
    if 3<=r<6 and c<3:
        return s_3
    if 3<=r<6 and 3<=c<6:
        return s_4
    if 3<=r<6 and c>=6:
        return s_5
    if r>=6 and c<3:
        return s_6
    if r>=6 and 3<=c<6:
        return s_7
    if r>=6 and c>=6:
        return s_8


def Num_Possible(Shudu):
    Count_Block_num(Shudu)
    num_p = np.zeros([9,9], dtype=int)
    all_num = set([0,1,2,3,4,5,6,7,8,9])
    s = set()
    k = set()
    num_0 = 0 #原来0的个数
    num_00 = 0 #消除的0的个数
    for i in range(9):
        for j in range(9):
            if Shudu[i][j] == 0:
                num_0 += 1
                for m in range(9):
                    s.add(Shudu[i][m])
                for n in range(9):
                    s.add(Shudu[n][j])
                k = Block_Num_P(Shudu, i, j)
                # print(s | k)
                num_p[i][j] = len(all_num-s)
                if num_p[i][j] == 1:
                    x = [y for y in all_num-s]
                    # print(x)
                    Shudu[i][j] = x[0]
                    num_p[i][j] = 0
                    num_00 += 1
            s.clear()
            k.clear()
    # print(num_00)
    # print(num_0)
    # print(Shudu)
    if num_0 > num_00 and num_00:
        Num_Possible(Shudu)
    else:
        print("[TIME] hh ", time.time() - start_time)
        SolveSudoku(Shudu)
    
    
                


def start_point(Shudu):
    for i in range(9):
        for j in range(9):
            if not Shudu[i][j]:
                return i, j
    return i, j


if __name__ == '__main__':
    
    start_time = time.time()
    # ans = SolveSudoku(Sudoku1)
    Num_Possible(Sudoku1)
    # print(Sudoku1)
    # aa = CheckSudokuCase(Sudoku1)
    # print(aa)
    print("[TIME]", time.time() - start_time)
    # print(ans)
    # print(Sudoku1)
