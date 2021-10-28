class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # if time O(n), space O(k), use maxHeap
        maxHeap = []
        for i in range(len(points)):
            point = points[i]
            heapq.heappush(maxHeap, [-self.distance_p(point), point])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        result = []
        while len(maxHeap) > 0:
            dist_neg, point = heapq.heappop(maxHeap)
            result.append(point)
        
        return result
        
    def distance_p(self, point):
        # no need to do root square
        return point[0]**2 + point[1]**2