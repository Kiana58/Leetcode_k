class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        answer = [0] * n
        
        # using stack method
        stack = []
        
        for curDay, curTemp in enumerate(temperatures):
            # if last day in the stack < curTemp, set that as the prevDay, calculate # of days for the prevDay
            # pop until stack is empty
            while stack and temperatures[stack[-1]] < curTemp:
                prevDay = stack.pop()
                answer[prevDay] = curDay - prevDay
            stack.append(curDay)
            
        return answer