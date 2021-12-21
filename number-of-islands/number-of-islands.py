from collections import deque
# directions
Directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # edge case: empty grid
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        # a set of (x, y) visited
        visited = set()
        
        # for every point, dfs
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if not sea and not visited
                if grid[i][j] == '1' and (i, j) not in visited:
                    islands += 1
                    self.bfs(grid, i, j, visited)
                    # print("i, j, visited: ", i, j, visited)
                    
        return islands
    
        # from (x, y), visit all island by bfs
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x,y))
        while queue:
            x, y = queue.popleft()
            # print("x,y,visited: ", x,y,visited)
            # for 4 directions of (x,y)
            for delta_x, delta_y in Directions:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
                
    # valid: in the grid and not in visited                
    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        # if out of bound
        if not (0<=x<n and 0<=y<m):
            return False
        # if already visited
        if (x, y) in visited:
            return False
        # if 1 then True, else 0 is False
        if grid[x][y] == '0':
            return False
        return True