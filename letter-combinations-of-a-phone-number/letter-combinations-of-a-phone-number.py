# put it outside of class
keyboard = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        combinations = []
        self.dfs(digits, 0, [], combinations)
        return combinations
    
    # the dfs which deal with digits[idx], combinations means current one, combinations are all founded results
    def dfs(self, digits, idx, combination, combinations):
        # recurisive outlet
        if idx == len(digits):
            combinations.append(''.join(combination))
            # just one digits, have to return if finished !!!
            return
            
        for letter in keyboard[digits[idx]]:
            combination.append(letter)
            self.dfs(digits, idx + 1, combination, combinations)
            combination.pop()