class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         # !!!!! use memoization method, where an array memomemo is used to store the result of the subproblems. 
#         @lru_cache
#         # method: two pointer and recursion
#         def wordBreakRecur(s, word_set, start):
#             # if recursion at end of s
#             if start == len(s):
#                 return True
#             for end in range(start+1, len(s) + 1):
#                 if s[start:end] in word_set and wordBreakRecur(s, word_set, end):
#                     return True
#             return False
            
#         return wordBreakRecur(s, frozenset(wordDict), 0)

        # method: DP
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]