class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums.sort()
        if not nums:
            return [[]]
        
        queue = [[]]
        idx = 0
        while idx < len(queue):
            subset = queue[idx]
            idx += 1
            for num in nums:
                if subset and subset[-1] >= num:
                    continue
                queue.append(subset + [num])
                
        return queue
        