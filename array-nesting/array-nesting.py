class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ######
        ## brute force method
        ######
#         n = len(nums)
#         res = 0 # record length of maximum set
        
#         def dfs(node):
#             if node in seen or len(seen) > n:
#                 # !!!! do not use break, break only for loops
#                 return
#             seen.add(node)
#             dfs(nums[node])
            
        
#         for i in range(n):
#             # every i, a set
#             seen = set()
#             dfs(nums[i])
#             res = max(res, len(seen))
        
#         return res

        ######
        ## visited array method: visited is for whole nums, not for nums[i]???
        ######

        self.maxClength= 0;
        self.visited= [False]*len(nums);
        
        for i in range( 0, len(nums)):
            self.dfs(nums, self.visited, i, 0);
            
        return self.maxClength;
    
    def dfs (self, nums, visited, i, count):
        if (visited[i] == True):
            self.maxClength= max(self.maxClength, count);
            return;

        if (visited[i] == False):
            visited[i]= True;
        self.dfs(nums, visited, nums[i], count+ 1);

        return;