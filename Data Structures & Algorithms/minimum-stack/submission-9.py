class MinStack:

    def __init__(self):

        self.data = []
        self.minStack = []
       

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.minStack or val <= self.minStack:
            self.minStack.append(val)
        
        

    def pop(self) -> None:
        x = self.data.pop()
        if x == self.mimStack[-1]:
            self.minStack.pop()


  

    def top(self) -> int:
        return self.data[-1]

 
       

    def getMin(self) -> int:
        return self.minStack[-1]

        