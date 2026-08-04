class MinStack:

    def __init__(self):
        self.stack=[]
        self.pstack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.pstack[-1] if self.pstack else val)
        self.pstack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.pstack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.pstack[-1]