import numpy as np
import time

class SolveMySudoku():
    def __init__(self):
        MySudoku = np.loadtxt('shudu.txt', dtype=int)
        self.SolveTheSudoku(MySudoku)


    def Smallest_Possibility_First_DFS(self, Blank, Row_Num, Col_Num, Block_Num, MySudoku):
        if len(Blank) == 0:
            print(MySudoku)
            return True

        All_Num = set(range(1,10))
        Smallest_Possible_Case = 9
        for (r,c) in Blank:
            Possibility = All_Num - ( Row_Num[r] | Col_Num[c] | Block_Num[r//3][c//3] )
            # print(Possibility, r, c)
            if len(Possibility) <= Smallest_Possible_Case:
                Smallest_Possible_Case = len(Possibility)
                i = r
                j = c
      
        if Smallest_Possible_Case == 0:
            return False

        # print("smallest: ", Possibility, r, c)
        Blank.remove((i, j))
        Possibility = All_Num - ( Row_Num[i] | Col_Num[j] | Block_Num[i//3][j//3] )
        
        for num in Possibility:
            Row_Num[i].add(num)
            Col_Num[j].add(num)
            Block_Num[i//3][j//3].add(num)
            MySudoku[i][j] = num
            if self.Smallest_Possibility_First_DFS(Blank, Row_Num, Col_Num, Block_Num, MySudoku):
                return True
            else:
                MySudoku[i][j] = 0
                Row_Num[i].remove(num)
                Col_Num[j].remove(num)
                Block_Num[i//3][j//3].remove(num)
    
        Blank.add((i, j))
        return False
    
    
    def SolveTheSudoku(self, MySudoku):

        Col_Num = []
        Row_Num = []
        Block_Num = [[0]*3 for i in range(3)]

        for i in range(9):
            Col_Num.append(set())
            Row_Num.append(set())
  
        for i in range(3):
            for j in range(3):
                Block_Num[i][j] = set()
  
        Blank = set()

        for i in range(9):
            for j in range(9):
                if MySudoku[i][j] != 0:
                    if MySudoku[i][j] not in Row_Num[i]:
                        Row_Num[i].add(MySudoku[i][j])
                    if MySudoku[i][j] not in Col_Num[j]:  
                        Col_Num[j].add(MySudoku[i][j])
                    if MySudoku[i][j] not in Block_Num[i//3][j//3]:   
                        Block_Num[i//3][j//3].add(MySudoku[i][j])
                else:
                    Blank.add((i,j))
  
        self.Smallest_Possibility_First_DFS(Blank, Row_Num, Col_Num, Block_Num, MySudoku)