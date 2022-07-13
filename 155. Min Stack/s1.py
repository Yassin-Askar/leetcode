class MinStack:

    def __init__(self):
        self.min_num = float('inf')
        self.stack = []
        pass

    def push(self, val: int) -> None:
        if val < self.min_num:
            self.min_num = val
        self.stack.append([val, self.min_num])

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min_num = self.stack[-1][1]
        else:
            self.min_num = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min_num
