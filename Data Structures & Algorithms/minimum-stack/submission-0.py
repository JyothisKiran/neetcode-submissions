class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        return None

    def pop(self) -> None:
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return min(self.stk)
