class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        # The minHeap for activate roome
        minHeap = []
        # count for minimum rooms needed
        min_rooms = 0

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])
        
        for meet in intervals:
            # while new meet start time is >= end time of one of the meeting
            # use while not if !!!!!
            while len(minHeap) > 0 and meet[0] >= minHeap[0][0]:
                heappop(minHeap)
            # push to minHeap (end, start), so minimum end time will be tracked
            heappush(minHeap, (meet[1], meet[0]))
            min_rooms = max(min_rooms, len(minHeap))
            
        return min_rooms
        
        

