class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # helper function to get result for one string
        def trimS(str1):
            result = []
            for s in str1:
                if s != '#':
                    result.append(s)
                # not else, because result need have value to pop
                elif result:
                    result.pop()
            return "".join(result)
        
        return trimS(s) == trimS(t)
