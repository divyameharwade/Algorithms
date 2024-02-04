# https://leetcode.com/problems/valid-sudoku/description/


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # bitwise
        # O(N) space and O(N2)time complexity
        # Use binary number to check previous occurrence
        
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    pos = int(board[r][c]) - 1
                    if rows[r] & (1 << pos): # -1 coz array is 0 indexed
                        return False
                    rows[r] |= (1 << pos)

                    if cols[c] & (1 << pos): # -1 coz array is 0 indexed
                        return False
                    cols[c] |= (1 << pos)

                    idx = (r//3) * 3 + c // 3 
                    if boxes[idx] & (1 << pos): # -1 coz array is 0 indexed
                        return False
                    boxes[idx] |= (1 << pos) 
        return True

        # # O(N2) space and time complexity
        # # check for duplicates in each row
        # for i in range(9):
        #     seen = set()
        #     for j in range(9):
        #         if board[i][j] != ".":
        #             if board[i][j] in seen:
        #                 return False
        #             seen.add(board[i][j])

        # # check number is repeated in entire col
        # for i in range(9):
        #     seen = set()
        #     for j in range(9):
        #         if board[j][i] != ".":
        #             if board[j][i] in seen:
        #                 return False
        #             seen.add(board[j][i])

        # # check for duplicates in each box
        # for row in [0, 3, 6]:
        #     for col in [0, 3, 6]:
        #         seen = set()
        #         for k in range(0 + row, 3 + row):
        #             for l in range(0 + col, 3 + col):
        #                 if board[k][l] != ".":
        #                     if board[k][l] in seen:
        #                         return False
        #                     seen.add(board[k][l])
        # return True
        
    
