from typing import List


def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = set()
    cols = set()
    for i in range(9):
        for j in range(9):
            row = board[i][j]
            col = board[j][i]
            if row in rows:
                return False
            if row != '.':
                rows.add(row)
            if col in cols:
                return False
            if col !='.':
                cols.add(col)
        rows.clear()
        cols.clear()
    row_min = col_min = 0
    row_max = col_max = 2
    box = set()
    for i in range(3):
        for j in range(3):
            for delta_x in range(row_min,row_max+1):
                for delta_y in range(col_min,col_max+1):
                    cur_char = board[delta_x][delta_y]
                    if cur_char in box:
                        return False
                    if cur_char != '.':
                        box.add(cur_char)
            box.clear()
            col_min +=3
            col_max+=3
        col_min=0
        col_max = 2
        row_min +=3
        row_max +=3
    return True
