class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # using 2 pointers
        left = 0
        for right in range(len(nums)):
            # if nums[right] == 1, no need to decrease/consume k
            k -= 1 - nums[right]
            
            # if all k are consumered by 0 from right, increase k from left side
            if k < 0:
                # if nums[left] == 0, move left + 1, increase k
                k += 1 - nums[left]
                left += 1
        return right - left + 1