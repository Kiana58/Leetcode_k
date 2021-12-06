class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # edge case
        if not position:
            return 0
        # move all odd position to 1, even position to 0
        position_01 = [num % 2 for num in position]
        
        # count # of 0 and 1, move less freq to more freq, cost is # of less freq one
        num_1 = sum(position_01)
        num_0 = len(position_01) - num_1
        
        return min(num_1, num_0)
        