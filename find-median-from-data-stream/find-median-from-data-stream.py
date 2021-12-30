class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # store lower half
        self.minHeap = [] # store larger half
        

    def addNum(self, num: int) -> None:
        # maxHeap length is equal or 1 larger than minHeap length
        heappush(self.maxHeap, -num)
        
        maxHeaptop = -heappop(self.maxHeap)
        heappush(self.minHeap, maxHeaptop)
        
        # balance two heaps
        if len(self.minHeap) > len(self.maxHeap):
            minHeaptop = heappop(self.minHeap)
            heappush(self.maxHeap, -minHeaptop)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + (-self.maxHeap[0]))/2.0
        else:
            return -self.maxHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()