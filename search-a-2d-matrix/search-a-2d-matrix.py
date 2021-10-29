class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        
        # transfer from matrix to sorted array
        start, end = 0, m*n - 1
        while start + 1 < end:
            mid = (start + end)//2
            row, col = self.idx_transfer(mid, n)
            if matrix[row][col] < target:
                start = mid
            else:
                end = mid
                
        row_s, col_s = self.idx_transfer(start, n)
        row_e, col_e = self.idx_transfer(end, n)
        
        if matrix[row_s][col_s] == target or matrix[row_e][col_e] == target:
            return True
        
        return False
        
    def idx_transfer(self, k, n):
        row = k // n
        col = k % n
        return row, col