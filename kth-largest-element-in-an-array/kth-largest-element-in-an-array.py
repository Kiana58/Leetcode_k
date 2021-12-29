class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # kth largest, pop n-k smallest
        minHeap = []
        
        for num in nums:
            heapq.heappush(minHeap, num)
            while len(minHeap) > k:
                heapq.heappop(minHeap)
                
        # return minHeap[0] !!!!
        return minHeap[0]