class MinStack:
    stack=[]
    pstack=[]
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
        if self.stack:
            return self.stack[-1]
        return 0
        

    def getMin(self) -> int:
        if self.pstack:
            return self.pstack[-1]
        else:
            return 0

        
