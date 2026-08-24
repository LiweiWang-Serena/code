class MinStack:

    def __init__(self):
        self.data = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self) -> None:
        x = self.data.pop()
        if x == self.minstack[-1]:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
