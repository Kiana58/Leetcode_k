class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # split version1 and 2 by .
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        idx_1, idx_2 = 0, 0
        
        while idx_1 < len(v1) and idx_2 < len(v2):
            if int(v1[idx_1]) < int(v2[idx_1]):
                return -1
            elif int(v1[idx_1]) > int(v2[idx_1]):
                return 1
            idx_1 += 1
            idx_2 += 1
            
        # at last element: idx_1 = idx_2
        # version1 still have element
        if idx_1 < len(v1) and int("".join(v1[idx_1:])) != 0: return 1
        # version2 still have element
        if idx_2 < len(v2) and int("".join(v2[idx_2:])) != 0: return -1
        
        return 0
        