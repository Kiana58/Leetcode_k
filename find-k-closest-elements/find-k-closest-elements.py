class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # from mid, assign left, right
        right = self.findupperclosest(arr,x)
        left = right - 1
        
        # expand from mid, like merge sort
        result = []
        for _ in range(k):
            # if left is closer, chose left side
            if self.isLeftcloser(arr, x, left, right):
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
        return sorted(result)
    
    def isLeftcloser(self, arr, x, left, right):
        # !!! needed, if no left elements
        if left < 0:
            return False
        # !!! if no right elements left, must do left side
        if right >= len(arr):
            return True
        # !!! <=, no <
        return x - arr[left] <= arr[right] - x
        
    # find most left >= target:
    def findupperclosest(self, arr, x):
        # find the mid
        start, end = 0, len(arr)-1
        while start + 1 < end:
            mid = (start + end)//2
            if arr[mid] >= x:
                end = mid
            else:
                start = mid
        
        # most left, so start with start
        if arr[start] >= x:
            return start
        if arr[end] >= x:
            return end
    
        # if could not find
        return len(arr)