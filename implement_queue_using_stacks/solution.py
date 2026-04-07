"""Implement Queue using Stacks"""
class Node:
    """Node class"""
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node
class Stack:
    """Stack class"""
    def __init__(self):
        self.head = None
    def push(self, item):
        """push docstring"""
        self.head = Node(item, next_node = self.head)
    def pop(self):
        """pop docstring"""
        dele = self.head.val
        self.head = self.head.next
        return dele
    def peek(self):
        """peek docstring"""
        return self.head.val
    def is_empty(self):
        """is_empty docstring"""
        return self.head is None
class MyQueue:
    """MyQueue class"""
    def __init__(self):
        self.start_stack = Stack()
        self.end_stack = Stack()
    def push(self, x: int) -> None:
        """ Pushes element x to the back of the queue."""
        self.start_stack.push(x)
    def pop(self) -> int:
        """Removes the element from the front of the queue and returns it"""
        if self.end_stack.is_empty():
            while True:
                if self.start_stack.is_empty():
                    break
                self.end_stack.push(self.start_stack.pop())
        return self.end_stack.pop()
    def peek(self) -> int:
        """Returns the element at the front of the queue."""
        if not self.end_stack.is_empty():
            return self.end_stack.peek()
        new_stack = Stack()
        while not self.start_stack.is_empty():
            new_stack.push(self.start_stack.pop())
        val = new_stack.peek()
        while not new_stack.is_empty():
            self.start_stack.push(new_stack.pop())
        return val
    def empty(self) -> bool:
        """Returns true if the queue is empty, false otherwise."""
        return self.start_stack.is_empty() and self.end_stack.is_empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
