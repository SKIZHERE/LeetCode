# 232. Implement Queue using Stacks

class MyQueue(object):

    def __init__(self):
        self.stack_in = []   # For push operations
        self.stack_out = []  # For pop and peek operations

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()  # Ensure stack_out has current elements
        return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_in and not self.stack_out
