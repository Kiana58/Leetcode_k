from heapq import *

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # create freqency map for tasks
        freqmap = {}
        for char in tasks:
            if char not in freqmap:
                freqmap[char] = 0
            freqmap[char] += 1
            
        # using maxHeap, put all freqmap to maxHeap
        maxHeap = []
        for char, freq in freqmap.items():
            heappush(maxHeap, (-freq, char))
            
        # pop most freq element everytime
        int_cnts = 0
        while maxHeap:
            queue = []
            # every block has k elements and the element
            n1 = n + 1
            # pop n distinct char to queue
            while maxHeap and n1 > 0:
                int_cnts += 1
                freq, char = heappop(maxHeap)
                if freq < -1:
                    queue.append((char, freq + 1))
                n1 -= 1
                
            # put it back to maxHeap
            for char, freq in queue:
                heappush(maxHeap, (freq, char))
                
            # have n idle intervals for next iteration
            if maxHeap:
                int_cnts += n1
                
        return int_cnts 
            
        
            
            
            
            
            
