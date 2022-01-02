class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
#         # similiar method:
#         count = 0
#         sums = 0
#         d = dict()
#         d[0] = 1
        
#         for i in range(len(nums)):
#             sums += nums[i]
#             count += d.get(sums-k,0)
#             d[sums] = d.get(sums,0) + 1
        
#         return count
        
        cur = 0
        n = len(nums)
        
        # defualtdict never raises a KeyError. It provides a default value for the key that does not exists.
        # for sum is x, how many subarrays, i.e, 2: sums[x] = 2
        sums = defaultdict(lambda: 0)
        sums[0] = 1          # Add 0 sum for the cases in which sum(0,i)=k
        
        ans = 0
        for i in range(n):
            cur += nums[i]
            ans += sums[cur-k]
            sums[cur] += 1
			
        return ans