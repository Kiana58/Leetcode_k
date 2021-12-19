class Solution:
    def decodeString(self, s: str) -> str:
        # method: stack
        stack = []
        for s1 in s:
            if s1 != ']':
                stack.append(s1)
            else:
                str_temp = []
                num = []
                while stack and stack[-1].isalpha():
                    p = stack.pop()
                    # str_temp.append(str(p))
                    str_temp = [p] + str_temp
                stack.pop()
                while stack and stack[-1].isdigit():
                    digit = stack.pop()
                    num = [digit] + num
                stack.append(int("".join(num)) * "".join(str_temp))
                # while str_temp:
                #     p_temp = str_temp.pop()
                #     stack.append(p_temp)
                    
        return "".join(stack)
        
        
        stack = []

        for char in s:
            if char!="]":
                stack.append(char)
            else:
                currStr = []
                num = []
                while stack and stack[-1].isalpha():
                    letter = stack.pop()
                    currStr = [letter] + currStr
                stack.pop()
                while stack and stack[-1].isdigit():
                    digit = stack.pop()
                    num = [digit] + num
                stack.append(int("".join(num)) * "".join(currStr))
            
        return "".join(stack)
                    
                    