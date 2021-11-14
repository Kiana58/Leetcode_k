class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.allCombinations = list(combinations(characters, combinationLength))
        self.count = 0

    def next(self) -> str:
        self.count += 1
        return "".join(self.allCombinations[self.count - 1])

    def hasNext(self) -> bool:
        return self.count < len(self.allCombinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()