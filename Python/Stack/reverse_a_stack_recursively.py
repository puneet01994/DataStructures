class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            print("Underflow")
            exit(1)
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0


def insert_at_bottom(stack, value):
    if stack.is_empty():
        stack.push(value)
    else:
        temp = stack.pop()
        insert_at_bottom(stack, value)
        stack.push(temp)


def reverse(stack):
    if not stack.is_empty():
        temp = stack.pop()
        reverse(stack)
        insert_at_bottom(stack, temp)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.data)

reverse(stack)

print(stack.data, "After reversal")
