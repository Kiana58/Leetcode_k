class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if len(s) == 0 or k == 0:
            return s
            
        freqm = {}
        for ss in s:
            if ss not in freqm:
                freqm[ss] = 0
            freqm[ss] += 1

        # dic to max heap
        maxHeap = []
        for char, freq in freqm.items():
            heappush(maxHeap, (-freq, char))

        # using deque
        queue = deque()
        resultS = []
        while maxHeap:
            freq, char = heappop(maxHeap)
            # append to resultS
            resultS.append(char)
            # decrement the freq, negative, so +1
            queue.append((char, freq + 1))
            if len(queue) == k:
                # if exact k, 
                char, freq = queue.popleft()
                # if freq < 0, delete the char in maxHeap
                if -freq > 0:
                    heappush(maxHeap, (freq, char))


        return ''.join(resultS) if len(resultS) == len(s) else ""
        
