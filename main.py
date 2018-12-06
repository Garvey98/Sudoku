import Solve_Sudoku
import Create_Sudoku
import numpy as np
import time
import sys

def main():

    # MySudoku = np.loadtxt('shudu.txt', dtype=int)
    time_start = time.time()
    para = sys.argv[1]
    if para == '-c':
        Sudoku_Count = int(sys.argv[2])
        Create_Sudoku.CreateMySudoku(Sudoku_Count)
    elif para == '-s':
        Sodoku_Path = sys.argv[2]
        Solve_Sudoku.SolveMySudoku(Sodoku_Path)
    else:
        print("Error Input")
    
    print("Using time: " , time.time()-time_start)



if __name__ == "__main__":
    main()