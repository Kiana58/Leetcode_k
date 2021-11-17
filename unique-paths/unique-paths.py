

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#         # Binary tree, dfs?
#         def dfs(i, j, m, n):
#             nonlocal count
#             # if out of range
#             if i > m -1 and j < n - 1:
#                 dfs(i, j+1, m, n)
#             if j > n - 1 and i < m -1 :
#                 dfs(i+1, j, m, n)
#             if i > m -1 and j > n -1:
#                 return
#             # if reach the end
#             if i == m-1 and j == n-1:
#                 count += 1
#             else:
#                 # only right or down
#                 dfs(i+1, j, m, n)
#                 dfs(i, j+1, m, n)
            
#         count = 0 
#         dfs(0, 0, m, n)
        
#         return count

        # Using DP
        dp = [[0 for _ in range(n)] for _ in range(m)]
    
        # make first row and col as 1
        for i in range(n):
            dp[0][i] = 1

        for i in range(m):
            dp[i][0] = 1


        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]