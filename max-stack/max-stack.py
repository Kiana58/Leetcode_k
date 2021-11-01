class MaxStack(object):

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if self.max_stack:
            number = max(self.max_stack[-1], x)
            self.max_stack.append(number)
        else:
            self.max_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.max_stack.pop()
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max_stack[-1]

    def popMax(self):
        """
        :rtype: int
        """
        max_num = self.peekMax()
        buffer_stack = []
        # pop until self.stack[-1] is max_num, pop to buffer_stack
        while self.top() != max_num:
            buffer_stack.append(self.pop())
        # when self.pop is max_num, pop
        self.pop()
        # put all buffer_stack back to stack and max_stack
        while buffer_stack:
            self.push(buffer_stack[-1])
            buffer_stack.pop()
            
        return max_num


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()