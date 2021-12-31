class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        patterns={}
        count=0
        for day in range(n):
            ones=[]
            # 1st and last cell always 0 because no 2 adjacent cells
            # ones: to record the index of 1 in current day
            for i in range(1,7):
                if cells[i-1]==  cells[i+1]:
                    ones.append(i)
            # cells: to record cells in current day
            cells=[1 if one in ones else 0 for one in range(8) ]
            
            # for large n: in string already transferred before as in pattern
            string=','.join([str(ret) for ret in cells])
            if string in patterns:
                keys=list(patterns.keys())
                a=keys[n%count-1]
                return [int(ret) for ret in (a.split(","))]
            patterns[string]=count
            count+=1
        return cells