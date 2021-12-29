class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # left record # of "(", right for # of ")"
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                res.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            # if # of ")" < # of "("
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
                
        backtrack()
        
        return res