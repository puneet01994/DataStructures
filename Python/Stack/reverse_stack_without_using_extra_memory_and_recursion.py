class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top is None:
            self.top = Node(value)

        else:
            node = Node(value)
            node.next = self.top
            self.top = node

    def pop(self):
        removedNode = self.top
        self.top = self.top.next
        return removedNode.value

    def reverse(self):
        curr = self.top
        prev = None
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.top = prev

    def print_stack(self):
        curr = self.top

        while curr:
            print(curr.value, end=" ")
            curr = curr.next


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.print_stack()
stack.reverse()
print()
stack.print_stack()