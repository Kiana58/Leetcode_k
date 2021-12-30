class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # method: using dic
        # step 1: build freq dic
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
            
        # step 2: transfer dic to list, sort the list by count
        lst = []
        for key, val in dic.items():
            lst.append((key, val))
            
        # sort tuples by descending second values
        lst.sort(key = lambda x : x[1], reverse=True)
        
        # step 3: get k most elements out
        res = []
        for i in range(k):
            res.append(lst[i][0])
        
        return res
        
        