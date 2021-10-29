class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        # from bottom left or upper right, row or column, one higher, one lower
        m, n = len(matrix), len(matrix[0])
        # start point, bottom left
        x, y = m-1, 0
        
        while x >= 0 and y <= n-1:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                # all same row are > target, could pass
                x -= 1
            else:
                y += 1
        
        return False
        