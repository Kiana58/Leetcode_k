directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # a set of (x, y) visited
        visited = set()
        self.bfs(image, sr, sc, visited, newColor, sr, sc)
        image[sr][sc] = newColor
        return image
    
    # method: bfs
    def bfs(self, image, x, y, visited, newColor, sr, sc):
        queue = deque([(x, y)])
        visited.add((x,y))
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if not self.is_valid(new_x, new_y, image, sr, sc, visited):
                    continue
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
                image[new_x][new_y] = newColor
            
    def is_valid(self, new_x, new_y, image, sr, sc, visited):
        n, m = len(image), len(image[0])
        # if out of bound
        if not (0<=new_x<n and 0<=new_y<m):
            return False
        # if already visited
        if (new_x, new_y) in visited:
            return False
        # if not same color
        if image[new_x][new_y] != image[sr][sc]:
            return False
        
        return True