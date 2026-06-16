class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        square = {}
        for r in range(9):
                for c in range(9):
                    val = board[r][c]
                    if val != '.' :
                            index = (r // 3) * 3 + (c // 3)
                            if val in square.get(index, '') :
                                return False
                            if val in col.get(c, '') :
                                return False
                            if val in row.get(r, '') :
                                return False
                            col[c] = col.get(c, '') + val 
                            row[r] = row.get(r, '') + val
                            square[index] = square.get(index, '') + board [r][c]
        return True
        