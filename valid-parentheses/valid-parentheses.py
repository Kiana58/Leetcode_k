class Solution:
    def isValid(self, s: str) -> bool:
        # edge case:
        if not s or len(s) == 1:
            return False
        
        
        dic = {')': '(',
               '}': '{',
               ']': '['}
        
        # method: use stack/list
        stack = []
        
        for s1 in s:
            # if (, [, {, append
            if s1 not in dic:
                stack.append(s1)
            # else, pop end of list
            else:
                if stack and stack[-1] == dic[s1]:
                    stack.pop()
                else:
                    return False
                
        return True if len(stack) == 0 else False