class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        # two pointer and recursion
        def wordBreakRecur(s, word_set, start):
            # if recursion at end of s
            if start == len(s):
                return True
            for end in range(start+1, len(s) + 1):
                if s[start:end] in word_set and wordBreakRecur(s, word_set, end):
                    return True
            return False
            
        return wordBreakRecur(s, frozenset(wordDict), 0)