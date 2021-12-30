directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set() #Backtracting
        def dfs(i, j, visited, count):
            if count == len(word):
                return True
            if i>=m or i<0 or j<0 or j>=n or (i,j) in visited or word[count]!=board[i][j]:
                return False
            visited.add((i,j))
            res = (dfs(i, j+1, visited, count+1) or
                dfs(i, j-1, visited, count+1) or
                dfs(i+1, j, visited, count+1) or
                dfs(i-1, j, visited, count+1))
            visited.remove((i,j))
            return res
                    
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]: #Check at each position
                    if dfs(i, j, visited, 0):
                        return True
        return False
#         def dfs(x, y, visited, count):
#             if count == len(word):
#                 return True
            
#             if self.is_valid(board, x, y, word[count], visited):
#                 visited.add((x, y))
#                 res = (dfs(x, y+1, visited, count+1) or
#                        dfs(x, y-1, visited, count+1) or
#                        dfs(x+1, y, visited, count+1) or
#                        dfs(x-1, y, visited, count+1))
                
#                 visited.remove((x, y))
#             return res
                    
#         visited = set()
#         for x in range(len(board)):
#             for y in range(len(board[0])):
#                 if board[x][y] == word[0]:
#                     if dfs(x, y, visited, 0):
#                         return True
#         return False
        
        
#     def is_valid(self, board, x, y, letter, visited):
#         n, m = len(board), len(board[0])
        
#         # if out of bound
#         if not (0 <= x < n and 0 <= y < m):
#             return False
#         # if already visited
#         if (x, y) in visited:
#             return False
#         # if not next letter
#         if board[x][y] != letter:
#             return False
        
#         return True
        