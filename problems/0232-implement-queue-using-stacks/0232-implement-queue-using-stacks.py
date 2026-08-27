class MyQueue:

    def __init__(self):
        self.stack_in = []   # For push operations
        self.stack_out = []  # For pop/peek operations

    def push(self, x: int) -> None:
        # Always push to the input stack
        self.stack_in.append(x)

    def pop(self) -> int:
        # Ensure the output stack has the oldest elements
        self._transfer()
        # Pop from the output stack (FIFO order)
        return self.stack_out.pop()

    def peek(self) -> int:
        # Ensure the output stack has the oldest elements
        self._transfer()
        # Look at the top of the output stack without removing it
        return self.stack_out[-1]

    def empty(self) -> bool:
        # The queue is empty if BOTH stacks are empty
        return not self.stack_in and not self.stack_out

    def _transfer(self) -> None:
        # If output stack is empty, move all elements from input stack to output stack
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()