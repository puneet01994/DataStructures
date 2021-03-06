class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top is None:
            return True
        return False

    def push(self, value):
        if self.top is None:
            self.top = Node(value)

        else:
            node = Node(value)
            node.next = self.top
            self.top = node

    def pop(self):
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value

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

    def clone(self, destination):
        self.reverse()
        curr = self.top
        while curr:
            destination.push(curr.value)
            curr = curr.next
        self.reverse()

    def reverse_recursively(self):
        if not self.isEmpty():
            temp = self.pop()
            self.reverse_recursively()
            self.insert_at_bottom(temp)

    def insert_at_bottom(self, data):
        if self.isEmpty():
            self.push(data)
        else:
            temp = self.pop()
            self.insert_at_bottom(data)
            self.push(temp)

    def print_stack(self):
        if self.top is None:
            print("Empty stack")
        curr = self.top

        while curr:
            print(curr.value, end=" ")
            curr = curr.next


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.print_stack()
# stack.reverse() and stack.reverse_recursively() both will give the same output.
stack.reverse_recursively()
print()
stack.print_stack()

# ------------- CLONE A STACK FROM SOURCE TO DESTINATION WITHOUT USING EXTRA SPACE ----------------
source = Stack()
source.push(1)
source.push(2)
source.push(3)
source.push(4)

destination = Stack()
print("Source stack was", )
source.print_stack()
print("Destination stack was")
destination.print_stack()
source.clone(destination=destination)
print("Source stack is now", )
source.print_stack()
print("Destination stack is now")
destination.print_stack()
