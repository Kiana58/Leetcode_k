class RandomizedSet(object):

    def __init__(self):
        # the dict: val as key, index as value
        self.nums, self.dict = [], {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        self.nums.append(val)
        self.dict[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        
        # put last element at val position to delete val in nums
        idx = self.dict[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.dict[last] = idx
        # delete last element
        self.nums.pop()
        # del val in dict
        del self.dict[val]
        
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        idx_chosen = random.randint(0, len(self.nums) - 1)
        return self.nums[idx_chosen]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()