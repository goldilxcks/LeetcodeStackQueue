"""Module"""
class Node:
    """Node class"""
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node
class Queue:
    """Queue class"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def is_empty(self):
        """check if empty"""
        return self.head is None
    def add(self, item):
        """add to end"""
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    def pop(self):
        """remove from front"""
        if self.is_empty():
            raise IndexError
        dele = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return dele
    def peek(self):
        """see first element"""
        if self.is_empty():
            raise IndexError
        return self.head.val
    def __len__(self):
        return self.size
    def __str__(self):
        return str(self.size)
class MyStack:
    """My Stack docstring"""
    def __init__(self):
        self.queue_start = Queue()
        self.queue_end = Queue()
    def push(self, x: int) -> None:
        """Pushes element x to the top of the stack."""
        self.queue_end.add(x)
        while not self.queue_start.is_empty():
            self.queue_end.add(self.queue_start.pop())
        self.queue_start, self.queue_end = self.queue_end, self.queue_start
    def pop(self) -> int:
        """Removes the element on the top of the stack and returns it"""
        return self.queue_start.pop()
    def top(self) -> int:
        """Returns the element on the top of the stack."""
        return self.queue_start.peek()
    def empty(self) -> bool:
        """Returns true if the stack is empty, false otherwise."""
        return self.queue_start.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
