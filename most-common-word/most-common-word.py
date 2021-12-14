class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # step 1: delete comma, ., ..., all to lowercase for paragraph
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = normalized_str.split()
        
        # freqmap for paragraph
        word_count = defaultdict(int)
        banned_words = set(banned)
        
        for word in words:
            if word not in banned_words:
                word_count[word] += 1
        
        # find the most frequent one but not in banned
        return max(word_count.items(), key=operator.itemgetter(1))[0]