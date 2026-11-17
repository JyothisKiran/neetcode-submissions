class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        square = {}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    if val in row.get(i,''):
                        return False
                    if val in col.get(j,''):
                        return False
                    sq = ((i//3)*3) + (j//3)
                    if val in square.get(sq,''):
                        return False
                    row[i] = row.get(i,'') + val
                    col[j] = col.get(j,'') + val
                    square[sq] = square.get(sq,'') + val
        return True
