import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # base case
        if not intervals:
            return 0
        # sort by start time
        intervals.sort()
        
        # using minHeap, put end time at first
        minHeap = []
        min_rooms = 0
        
        for i in range(len(intervals)):
            st, end = intervals[i][0], intervals[i][1]
            # use while not if !!!! while next meeting's start time >= min meeting's end time, pop one room, minHeap[0] not minHeap[-1] !!!
            while len(minHeap) > 0 and st >= minHeap[0][0]:
                heappop(minHeap)
            heappush(minHeap, (end, st))
            
            # every step, check maximum!!!
            min_rooms = max(min_rooms, len(minHeap))
                
        return min_rooms