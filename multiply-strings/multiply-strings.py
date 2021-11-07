class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # m, n = len(num1), len(num2)
        
        # for every n2 digit, multiple to num1
        # get num1_num
        num1_num = 0
        res = 0
        
        for n1 in num1:
            num1_num = num1_num * 10 + int(n1)
            print("num1_num: ", num1_num)
        for n2 in num2:
            res = res * 10 + num1_num * int(n2)
            print("res: ", res)
                
        return str(res)
        
                