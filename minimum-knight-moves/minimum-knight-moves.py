from collections import deque

offsets = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]

class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # add source
        queue = deque([(0, 0)])
        # a map to record source to (x,y) shortest distance
        cell_to_dis_dict = {(0, 0):0}
        
        while queue:
            x_new, y_new = queue.popleft()
            if (x_new, y_new) == (x, y):
                return cell_to_dis_dict[(x_new, y_new)]
            for dx, dy in offsets:
                next_x, next_y = x_new + dx, y_new + dy
                # if not self.is_valid(next_x, next_y):
                #     continue
                if (next_x, next_y) in cell_to_dis_dict:
                    continue
                queue.append((next_x, next_y))
                cell_to_dis_dict[(next_x, next_y)] = cell_to_dis_dict[(x_new, y_new)] + 1
        return -1
    
    # infinite board, no barrier
    # def is_valid(self, x, y):
    #     return not grid[x][y]