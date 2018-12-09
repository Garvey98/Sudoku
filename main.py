#!/usr/bin/python3
""" This is function main"""
import time
import sys
import solve_sudoku
import create_sudoku

def main():
    """ This is function main"""
    time_start = time.time()
    para = sys.argv[1]
    if para == '-c':
        sudoku_count = int(sys.argv[2])
        create_sudoku.CreateMySudoku(sudoku_count)
    elif para == '-s':
        sodoku_path = sys.argv[2]
        solve_sudoku.SolveMySudoku(sodoku_path)
    else:
        print("Error Input")

    print("Using time: ", time.time()-time_start)



if __name__ == "__main__":
    main()
