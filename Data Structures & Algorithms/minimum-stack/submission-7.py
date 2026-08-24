class MinStack:

    def __init__(self): #initialize 
        self.main = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.main.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        

    def pop(self) -> None:
        x = self.main.pop()
        if x == self.minStack[-1]:
            self.minStack.pop()
       

    def top(self) -> int:
        return self.main[-1]
       

    def getMin(self) -> int:
        return self.minStack[-1]
        