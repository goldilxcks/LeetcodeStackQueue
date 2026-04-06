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
        """Push item to top"""
        self.head = Node(item, self.head)

    def pop(self):
        """Remove top item"""
        if self.head is None:
            raise IndexError
        value = self.head.val
        self.head = self.head.next
        return value

    def peek(self):
        """Return top item"""
        if self.head is None:
            raise IndexError
        return self.head.val

    def is_empty(self):
        """Check if stack is empty"""
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
        self.val_head = None
        self.grp_head = None
        self.max_freq = 0

    def push(self, val: int) -> None:
        """Pushes an integer val onto the top of the stack."""
        val_node = self.val_head
        while val_node is not None:
            if val_node.val == val:
                break
            val_node = val_node.next
        if val_node is None:
            self.val_head = ValueFreqNode(val, 1, self.val_head)
            val_node = self.val_head
        else:
            val_node.freq += 1
        frq = val_node.freq
        grp_node = self.grp_head
        if grp_node is None or grp_node.freq == frq:
            if grp_node is None:
                self.grp_head = FreqGroupNode(frq)
                grp_node = self.grp_head
            else:
                grp_node.stack.push(val)
                if frq > self.max_freq:
                    self.max_freq = frq
                return
        else:
            while grp_node.next is not None and grp_node.next.freq != frq:
                grp_node = grp_node.next
            if grp_node.next is None:
                grp_node.next = FreqGroupNode(frq)
            grp_node = grp_node.next
        grp_node.stack.push(val)
        if frq > self.max_freq:
            self.max_freq = frq

    def pop(self) -> int:
        """Removes and returns the most frequent element in the stack."""
        grp_node = self.grp_head
        if grp_node is None:
            raise IndexError
        if grp_node.freq == self.max_freq:
            value = grp_node.stack.pop()
            if grp_node.stack.is_empty():
                self.grp_head = grp_node.next
                self.max_freq -= 1
        else:
            while grp_node.next is not None and grp_node.next.freq != self.max_freq:
                grp_node = grp_node.next
            target_group = grp_node.next
            value = target_group.stack.pop()
            if target_group.stack.is_empty():
                grp_node.next = target_group.next
                self.max_freq -= 1
        val_node = self.val_head
        while val_node is not None:
            if val_node.val == value:
                val_node.freq -= 1
                break
            val_node = val_node.next
        return value
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
