class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # method: sorted, then 2 pointer
        arr.sort()
        
        n, idx = len(arr), 0
        min_diff = math.inf
        ans = []
        # 1st step: find min_diff
        for idx in range(n-1):
            diff_lr = arr[idx+1] - arr[idx]
            min_diff = min(min_diff, diff_lr)
            
        # 2nd step: find the array with min_diff
        for idx in range(n-1):
            diff_lr = arr[idx+1] - arr[idx]
            if diff_lr == min_diff:
                ans.append([arr[idx], arr[idx+1]])
                
        return ans
        
        