from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()  # Main queue, holds stack elements
        self.q2 = deque()  # Helper queue

    def push(self, x: int) -> None:
        self.q2.append(x)                 # 1. Add new element to helper queue
        while self.q1:                    # 2. Move all from main to helper
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1 # 3. Swap them

    def pop(self) -> int:
        return self.q1.popleft()          # The front of q1 is the stack's top

    def top(self) -> int:
        return self.q1[0]                 # Peek at the front of q1

    def empty(self) -> bool:
        return len(self.q1) == 0