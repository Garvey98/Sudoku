#!/usr/bin/python3
""" This is function main"""
import time
import sys
import solve_sudoku
import create_sudoku


def main():
    """ This is function main"""
    try:
        time_start = time.time()
        para = sys.argv[1]
        if para == '-c':
            sudoku_count = int(sys.argv[2])
            if sudoku_count <= 0:
                raise ValueError
            create_sudoku.CreateMySudoku(sudoku_count)

        elif para == '-s':
            sodoku_path = sys.argv[2]
            solve_sudoku.SolveMySudoku(sodoku_path)
        else:
            print("Invalid command.")
            print("You can type the command 'python main.py' to view valid commands.")

    except ValueError:
        print("The second argument should be a positive integer.")
    except IOError as err:
        print("File does not exist.", err)
    except IndexError:
        print("Need two parameters, here is how to use it:")
        print("[Type the command]`python main.py -c 100`: Generate 100 sudoku endings.")
        print("[Type the command]`python main.py -s \"Sudoku_Problem.txt\"`: \
            Solve the sudoku in \"Sudoku_Problem.txt\".")

    finally:
        print("Using time: ", time.time()-time_start)


if __name__ == "__main__":
    main()
