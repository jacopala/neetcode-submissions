class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        return None

    def pop(self) -> None:
        self.stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        res=int(self.stack[0])
        for n in range(1,len(self.stack)):
            if self.stack[n]<res:
                res=self.stack[n]
        return res