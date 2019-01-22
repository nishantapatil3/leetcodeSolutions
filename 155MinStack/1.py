class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.a = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.a:
            self.a.append((x,x))
        else:
            self.a.append((x, min(x,self.a[-1][1])))

    def pop(self):
        """
        :rtype: void
        """
        if self.a:
            return self.a.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.a:
            return self.a[-1][0]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.a:
            return self.a[-1][1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
