class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # find the index to remove
        idx_remove = set()
        
        # go through, let # of ( == # of ) by poping (
        stack = []
        for idx, char in enumerate(s):
            if char not in "()":
                continue
            elif char == '(':
                stack.append(idx)
            # if # of ( != # of ), stack is empty
            elif not stack:
                idx_remove.add(idx)
            else:
                stack.pop()
                
        # !!! at the end, maybe stack is not empty, need union stack and idx_remove together
        idx_remove = idx_remove.union(set(stack))
        
        # go through s, put all except idx_remove
        result = []
        for idx, char in enumerate(s):
            if idx not in idx_remove:
                result.append(char)
                
        return ''.join(result)