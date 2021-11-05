class Solution:
    def arrangeCoins(self, n: int) -> int:
        row, sum_k = 1, 1
        while sum_k <= n:
            row += 1
            sum_k += row
        return row-1
        