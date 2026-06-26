class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for c in range(9):
            for r in range(9):
                if (board[c][r] == "."):
                    continue
                elif (board[c][r] in rows[r] or
                      board[c][r] in cols[c] or
                      board[c][r] in squares[(c//3, r//3)]):
                    return False
                cols[c].add(board[c][r])
                rows[r].add(board[c][r])
                squares[(c//3,r//3)].add(board[c][r])
        return True