from collections import defaultdict
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if(board[r][c] == "."):
                    continue
                if (board[r][c] in rows[r] or 
                   board[r][c] in cols[c] or 
                   board[r][c] in squares[(r//3,c//3)]):
                   return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        # print(rows)
        # print(cols)
        # print(squares)
        return True

sudokuboard = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

isValidSudoku(sudokuboard)