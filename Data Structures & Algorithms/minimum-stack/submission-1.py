class MinStack:

    def __init__(self):
        """ Initate 2 stacks, one stack that holds the value, one minStack
            that keeps track of the minimum
        """

        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Append value to the stack
        self.stack.append(val)
        # Compare the value with the current minimum if it exists
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)
    def pop(self) -> None:
        # Pop the value
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]

        
