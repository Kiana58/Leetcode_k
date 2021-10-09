class FreqStack(object):

    def __init__(self):
        # create freqmap dic
        self.freq = collections.Counter()
        # create dic for stack, if x has n elements, push it n times in stackdic[1], stackdic[2], ...stackdic[m]
        # the type is list for stackdic[1], it could also be int, set... in other cases
        self.stackdic = collections.defaultdict(list)
        # maxf records current max frequency for all elements
        self.maxf = 0


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        freq, stackdic = self.freq, self.stackdic
        # push val
        # update freq[val] and maxf
        freq[val] += 1
        self.maxf = max(self.maxf, freq[val])
        # update stackdic
        self.stackdic[freq[val]].append(val)

    def pop(self):
        """
        :rtype: int
        """
        # pop most freq, then last added value
        freq, stackdic, maxf = self.freq, self.stackdic, self.maxf
        x = stackdic[maxf].pop()
        # update stackdic
        if not stackdic[maxf]:
            self.maxf = maxf - 1
        # update freq
        freq[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
