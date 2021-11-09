class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dic = { ')': '(',
                ']': '[',
                '}': '{'
        }
        for s1 in s:
            if s1 in list(dic.values()):
                stack.append(s1)
            else:
                if stack and stack[-1] == dic[s1]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False