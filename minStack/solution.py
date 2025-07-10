class MinStack:

    def __init__(self):
        self.Stack =[]
        self.minStack=[]
        
    def push(self, val: int) -> None:
        self.Stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            if self.minStack[-1] < val:
                self.minStack.append(self.minStack[-1])
            else:
                self.minStack.append(val)

        return None
        
    def pop(self) -> None:
        self.minStack.pop()
        self.Stack.pop()
        return None

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


        
