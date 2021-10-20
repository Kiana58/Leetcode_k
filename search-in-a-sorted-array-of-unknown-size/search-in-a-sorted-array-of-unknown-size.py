# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # find idx where secret[idx] < target
        idx = 1
        while reader.get(idx-1) <= target:
            idx = idx*2
            
        # Binary search to find the idx where target is
        start, end = 0, idx-1
        while start + 1 < end:
            mid = (start + end)//2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
                
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        # this is needed if nothing find !!!!
        return -1