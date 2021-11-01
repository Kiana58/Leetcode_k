class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    # stack2 is like reverse of stack1
    def stack1_to_stack2(self):
        # if stack2 is not empty, do not reverse stack1!!!!!
        if self.stack2:
            return
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.stack1_to_stack2()
        return self.stack2.pop()
        

    def peek(self):
        """
        :rtype: int
        """      
        self.stack1_to_stack2()
        return self.stack2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return True if len(self.stack1) == 0 and len(self.stack2) == 0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()