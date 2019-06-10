class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.maxEle = None

    def __str__(self):
        temp = self.top
        max_ele = self.maxEle

        stack = []

        while temp:
            x = temp.value
            if x > max_ele:
                prev_max = 2 * max_ele - x
                x = (x + prev_max) / 2
                max_ele = prev_max

            stack.append(int(x))
            temp = temp.next
        return stack

    def getMax(self):
        if self.top is None:
            return "Empty stack"

        else:
            return self.maxEle

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.maxEle = value

        elif value > self.maxEle:
            temp = 2 * value - self.maxEle
            node = Node(temp)
            node.next = self.top
            self.top = node
            self.maxEle = value

        else:
            node = Node(value)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return "Empty stack"

        else:
            temp = self.top
            self.top = self.top.next

            if temp.value > self.maxEle:
                x = temp.value
                if x > self.maxEle:
                    prev_max = 2 * self.maxEle - x
                    x = (x + prev_max) / 2

                self.maxEle = 2 * self.maxEle - temp.value
                return "{} removed".format(x)
            else:
                return "{} removed".format(temp.value)


new_stack = Stack()

new_stack.push(2)
new_stack.push(4)
new_stack.push(5)
new_stack.push(3)
new_stack.push(8)

data = new_stack.pop()
print(data)

stack = new_stack.__str__()
print(stack)
print(new_stack.maxEle)
