class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic_num2let = {
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        # edge case, empty digits
        if not digits or len(digits) == 0:
            return []
        
        res = []
        
        def backtrack(index, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            for letter in dic_num2let[digits[index]]:
                path.append(letter)
                # move to next digit in digits
                backtrack(index+1, path)
                # backtrack by removing the letter before moving onto the next
                path.pop()
                
        backtrack(0, [])
                
        return res