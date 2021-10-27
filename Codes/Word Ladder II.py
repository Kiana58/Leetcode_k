class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        wordList.add(beginWord)
        wordList.add(endWord)
        
        # records of shortest path from biginWord
        distance = {}
        
        # records of from one word, all next word (with possible shortest path)
        fromToDict = {}
        
        for s in wordList:
            fromToDict[s] = []
        self.bfs(beginWord, fromToDict, distance, wordList)
        
        # for shortest path
        results = []
        self.dfs(beginWord, endWord, distance, wordList, [], results, fromToDict, distance[endWord])
        
        return results
    
    def bfs(self, start, fromToDict, distance, d):
        distance[start] = 0
        queue = deque([start])
        
        while queue:
            curr_word = queue.popleft()
            for next_word in self.get_next_words(curr_word, d):
                if (next_word not in distance or distance[next_word] == distance[curr_word]+1):
                    fromToDict[curr_word].append(next_word)
                    
                # if next word not exists, record from start, to every word, the shortest path, then find the word from nextWord
                if next_word not in distance:
                    distance[next_word] = distance[curr_word] + 1
                    queue.append(next_word)
                    
    def dfs(self, curr_word, target, distance, d, path, results, fromToDict, min_len):
        if len(path) == min_len + 1:
            return

        path.append(curr_word)

        if curr_word == target:
            results.append(list(path))
        else:
            for nextWord in fromToDict[curr_word]:
                self.dfs(nextWord, target, distance, d, path, results, fromToDict, min_len)

        path.pop()
            
    def get_next_words(self, word, d):
        words = []
        for i in range(len(word)):
            for c in string.ascii_lowercase:
                if (word[i] == c):
                    continue;
                next_word = word[:i] + c + word[i+1:]
                if next_word in d:
                    words.append(next_word)

        return words
                
        
