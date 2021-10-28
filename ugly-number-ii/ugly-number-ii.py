class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        minHeap = [1]
        # no duplicated, not set(1)
        seen = set([1])
        
        # nth number....!!!!
        for _ in range(n):
            # current smallest ugly number
            curr_ugly = heapq.heappop(minHeap)
            for factor in [2,3,5]:
                new_ugly = curr_ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(minHeap, new_ugly)
                
            
        return curr_ugly