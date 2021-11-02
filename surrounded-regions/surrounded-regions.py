DIRECTIONS = [(1,0), (-1, 0), (0, 1), (0, -1)]
from itertools import product

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if board is None or len(board) == 0:
            return
        
        # using dfs, from boarders of board, if connected with board O, do not change, else change O to X
        boarders = list(product(range(m), [0, n-1])) + list(product([0, m-1], range(n)))
        
        # dfs find all Os connected with O in boards, mark them as E
        for row, col in boarders:
            self.dfs(board, row, col, m, n)
            
        # go through all board, O -> X, E -> O
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'E':
                    board[r][c] = 'O'
            
    def dfs(self, board, row, col, m, n):
        # if out of range
        if row < 0 or row >= m or col < 0 or col >= n:
            return
        # if no O, return
        if board[row][col] != 'O':
            return
        # else all O to E
        board[row][col] = 'E'
        # for column not at boarders
        for r, c in DIRECTIONS:
            self.dfs(board, row+r, col+c, m, n)