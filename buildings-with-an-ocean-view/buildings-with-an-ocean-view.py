class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if not heights:
            return []
        idx = len(heights) - 1
        max_height = heights[-1]
        res = [idx]
        while idx > 0:
            idx -= 1
            if heights[idx] > max_height:
                res.append(idx)
                max_height = heights[idx]
        return res[::-1]
                
            
            
            