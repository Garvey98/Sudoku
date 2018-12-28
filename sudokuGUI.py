import tkinter as tk
from tkinter import messagebox
import random
import numpy as np


window = tk.Tk()
window.title('sudoku')
window.geometry('600x600')


sudoku = np.array([[1, 9, 6, 4, 3, 8, 7, 5, 2],
                   [3, 8, 4, 5, 7, 2, 1, 6, 9],
                   [7, 2, 5, 6, 1, 9, 3, 4, 8],
                   [5, 7, 2, 1, 6, 3, 9, 8, 4],
                   [6, 3, 1, 8, 9, 4, 5, 2, 7],
                   [9, 4, 8, 2, 5, 7, 6, 1, 3],
                   [2, 5, 7, 9, 4, 1, 8, 3, 6],
                   [4, 1, 9, 3, 8, 6, 2, 7, 5],
                   [8, 6, 3, 7, 2, 5, 4, 9, 1]])


def change_root(shudu):
    """ Change sudoku map"""
    numofexchange = 1
    temp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while numofexchange < 10:
        random.shuffle(temp_list)
        random_num = temp_list[1]
        if random_num == 9:
            for i in range(9):
                for j in range(9):
                    if shudu[i][j] == random_num:
                        shudu[i][j] = 1
                    elif shudu[i][j] == 1:
                        shudu[i][j] = 9
        else:
            for i in range(9):
                for j in range(9):
                    if shudu[i][j] == random_num:
                        shudu[i][j] = random_num+1
                    elif shudu[i][j] == random_num+1:
                        shudu[i][j] = random_num
        numofexchange += 1
    return shudu


def rowcolumn_exchange(shudu):
    """ Row and column transformation"""
    numofexchange = 1
    temp_list = [1, 2, 3, 4, 5, 6, 7, 8]
    while numofexchange < 4:
        random.shuffle(temp_list)
        rownum = temp_list[1]
        if (rownum % 3) == 2:
            shudu[[rownum, rownum-1], :] = shudu[[rownum-1, rownum], :]
        else:
            shudu[[rownum, rownum+1], :] = shudu[[rownum+1, rownum], :]
        shudu = shudu.T
        numofexchange += 1
    return shudu


EntryList = []
s = set()
# tk.Text(window,height=1, width=5).grid(row = 15)


def newproblem(shudu):
    temp_list1 = [4, 5, 6]
    temp_list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for row in range(9):
        random.shuffle(temp_list1)
        num1 = temp_list1[1]
        random.shuffle(temp_list2)
        for col in range(num1):
            shudu[row][temp_list2[col]] = 0
    return shudu


def solving_sudoku():
    col_num = []
    row_num = []
    sqr_num = [[0]*3 for _ in range(3)]

    for i in range(9):
        col_num.append(set(tuple(range(1, 10))))
        row_num.append(set(tuple(range(1, 10))))

    for i in range(3):
        for j in range(3):
            sqr_num[i][j] = set(tuple(range(1, 10)))
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                if sudoku[i][j] in row_num[i]:
                    row_num[i].remove(sudoku[i][j])
                if sudoku[i][j] in col_num[j]:
                    col_num[j].remove(sudoku[i][j])
                if sudoku[i][j] in sqr_num[i//3][j//3]:
                    sqr_num[i//3][j//3].remove(sudoku[i][j])

    tag = 1
    for i in range(9):
        if len(row_num[i]) != 0:
            tag = 0
        if len(col_num[i]) != 0:
            tag = 0
    for i in range(3):
        for j in range(3):
            if len(sqr_num[i][j]):
                tag = 0
    return tag


def insert_end():
    try:
        for (row, col) in s:
            sudoku[row][col] = EntryList[row*9+col].get()
        tag = solving_sudoku()
        if tag == 1:
            tk.messagebox.showinfo(title='恭喜', message='正确')
        else:
            tk.messagebox.showinfo(title='糟糕', message='检查一下哦，有些地方好像不对！')
    except Exception:
        tk.messagebox.showinfo(title='未完成数独', message='还有空格没有填入数字哦！')


def show(shudu):
    for i in range(9):
        for j in range(9):
            if shudu[i][j] == 0:
                EntryList.append(tk.Entry(window, font=("Calibri", 12), justify="center", width=6, fg="black",
                                          highlightbackground="black", highlightcolor="red", highlightthickness=1, bd=0))
                EntryList[i*9+j].grid(row=i, column=j, ipady=14)
                s.add((i, j))
            else:
                EntryList.append(
                    tk.Label(window, text=shudu[i][j], font=("Calibri", 12), width=6))
                EntryList[i*9+j].grid(row=i, column=j, ipady=14)


sudoku = change_root(sudoku)
sudoku = rowcolumn_exchange(sudoku)
print(sudoku)
sudoku = newproblem(sudoku)
show(sudoku)
b2 = tk.Button(window, text="提交", command=insert_end)
b2.grid(row=12, column=5)
window.mainloop()
