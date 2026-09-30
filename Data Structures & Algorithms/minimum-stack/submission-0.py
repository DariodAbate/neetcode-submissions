class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val: int) -> None:

        if not self.stack or val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        
        self.stack.append(val)
        

    def pop(self) -> None:
        self.min.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
