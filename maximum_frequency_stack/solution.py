"""Module"""
class Node:
    """Node for linked structures"""
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class Stack:
    """Stack class"""
    def __init__(self):
        self.head = None
    def push(self, item):
        """push docstring"""
        self.head = Node(item, next_node=self.head)
    def pop(self):
        """pop docstring"""
        if self.head is None:
            raise IndexError
        dele = self.head.val
        self.head = self.head.next
        return dele
    def peek(self):
        """peek docstring"""
        if self.head is None:
            raise IndexError
        return self.head.val
    def is_empty(self):
        """is_empty docstring"""
        return self.head is None

class ValueFreqNode:
    """Class for nodes values and frequencies"""
    def __init__(self, val, freq=0, next_node=None):
        self.val = val
        self.freq = freq
        self.next = next_node

class FreqGroupNode:
    """Class for groups of different frequency"""
    def __init__(self, freq, next_node=None):
        self.freq = freq
        self.stack = Stack()
        self.next = next_node

class FreqStack:
    """Frequency Stack class"""
    def __init__(self):
        self.values_head = None
        self.groups_head = None
        self.max_freq = 0
    def push(self, val: int) -> None:
        """pushes an integer val onto the top of the stack."""
        curr_1 = self.values_head
        value_node = None
        while curr_1:
            if curr_1.val == val:
                value_node = curr_1
                break
            curr_1 = curr_1.next
        if value_node is None:
            value_node = ValueFreqNode(val, 0, self.values_head)
            self.values_head = value_node
        value_node.freq += 1
        new_freq = value_node.freq
        curr_2 = self.groups_head
        group_node = None
        while curr_2:
            if curr_2.freq == new_freq:
                group_node = curr_2
                break
            curr_2 = curr_2.next
        if group_node is None:
            group_node = FreqGroupNode(new_freq, self.groups_head)
            self.groups_head = group_node
        group_node.stack.push(val)
        if new_freq > self.max_freq:
            self.max_freq = new_freq

    def pop(self) -> int:
        """removes and returns the most frequent element in the stack."""
        curr = self.groups_head
        last = None
        group = None
        while curr:
            if curr.freq == self.max_freq:
                group = curr
                break
            last = curr
            curr = curr.next
        first = group.stack.pop()
        current = self.values_head
        while current:
            if current.val == first:
                current.freq -= 1
                break
            current = current.next
        if group.stack.is_empty():
            if last is None:
                self.groups_head = group.next
            else:
                last.next = group.next
            self.max_freq -= 1
        return first
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
