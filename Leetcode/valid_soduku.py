from typing import List
import collections


class Solution:
    '''This is to return a soduku is valid or not 9x9 soduku board, o(n^2) or 9^2'''

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        # it's for 3x3 boxes, input set will be (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if (board[r][c] == '.'):
                    continue
                elif (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[(r // 3, c // 3)]
                ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True


s = Solution()

print(s.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
    "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(s.isValidSudoku([[".", "8", "7", "6", "5", "4", "3", "2", "1"], ["2", ".", ".", ".", ".", ".", ".", ".", "."], ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", ".", ".", ".", ".", "."], [
      "5", ".", ".", ".", ".", ".", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."], ["9", ".", ".", ".", ".", ".", ".", ".", "."]]))
