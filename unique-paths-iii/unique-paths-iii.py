DIRECTIONS = [(0,1), (0, -1), (1, 0), (-1, 0)]
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        # find start point & count all empty squares
        start, count = None, 0
        for i in range(m):
            for j in range(n):
                count += grid[i][j] == 0
                if not start and grid[i][j] == 1:
                    start = (i, j)
                    
        def backtrack(i, j):
            # find all valid path from start point (i, j), return # of valid paths
            
            nonlocal count
            result = 0
            for dx, dy in DIRECTIONS:
                x, y = i+dx, j+dy
                if 0<= x < m and 0 <= y < n:
                    # if empty, visited, flagged as obstacle
                    if grid[x][y] == 0:
                        grid[x][y] = -1
                        count -= 1
                        result += backtrack(x, y)
                        # backtrack and reset
                        grid[x][y] = 0
                        count += 1
                    elif grid[x][y] == 2:
                        # if at the end, check if all squares have been walked over
                        result += count == 0
            return result
        
        return backtrack(start[0], start[1])
        