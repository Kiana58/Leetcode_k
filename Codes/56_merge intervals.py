class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort by first number
        intervals.sort()
        n = len(intervals)
        merged = [intervals[0]]
        for i in range(1, n):
            # !!! compare one interval with the one in the merged list !!!
            st1, end1 = merged[-1]
            st2, end2 = intervals[i]
            if end1 < st2:
                # no need to change, just append
                merged.append(intervals[i])
            else:
                st = min(st1, st2)
                end = max(end1, end2)
                # updated last element in merged list
                merged[-1] = st, end
                
        return merged
            
            
