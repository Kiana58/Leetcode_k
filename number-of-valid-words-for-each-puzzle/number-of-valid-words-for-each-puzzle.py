class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # Kiana brute force solution....
        # answer = []
        # for puzzle in puzzles:
        #     letter_1st = puzzle[0]
        #     puzzle_set = set(puzzle)
        #     cnt = 0
        #     for i in range(len(words)):
        #         word = words[i]
        #         word_set = set(word)
        #         # if word do not have 1st letter of puzzle, move to next word
        #         if letter_1st not in word_set:
        #             i += 1
        #         else:
        #             word_len = 0
        #             for char in word:
        #                 # if the letter is not in puzzle
        #                 if char not in puzzle_set:
        #                     i += 1
        #                     break
        #                 else:
        #                     word_len += 1
        #             if word_len == len(word): 
        #                 cnt += 1
        #     answer.append(cnt)
        # return answer
        
        # from solution and discussion
        trie = Trie()
        for word in words:
            trie.add(word)
        return [trie.search(word) for word in puzzles]
    
class TrieNode:
    def __init__(self, ch: Optional[str] = ''):
        self.ch = ch
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children.keys():
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]
        node.count += 1
    
    def search(self, word: str) -> int:       
        def dfs(node: TrieNode, found: Optional[bool] = False) -> int:
            result = node.count*found
            for ch in word:
                if ch in node.children.keys():
                    result += dfs(node.children[ch], found or ch == word[0])
            return result
        return dfs(self.root)
        
                    
                