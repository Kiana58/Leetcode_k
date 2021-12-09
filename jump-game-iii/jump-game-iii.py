class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        
        # edge case
        if 0 <= start < len(arr) and arr[start] >= 0:
            # outlet
            if arr[start] == 0:
                return True
            arr[start] = -arr[start]
            return self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])

        return False