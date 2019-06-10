class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.minEle = None
        self.maxEle = None

    def __str__(self):
        temp = self.top
        stack = []
        min_value = self.minEle

        while temp:
            x = temp.value
            if temp.value < min_value:
                prev_min_element = 2 * min_value - temp.value
                x = (prev_min_element + x)/2
                min_value = prev_min_element

            stack.append(int(x))
            temp = temp.next

        return self.top.value, stack

    def getMin(self):
        if self.top is None:
            return "Empty stack"

        else:
            return self.minEle

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.minEle = value

        elif value < self.minEle:
            temp = 2 * value - self.minEle
            node = Node(temp)
            node.next = self.top
            self.top = node
            self.minEle = value

        else:
            node = Node(value)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return "Empty stack."

        else:
            temp = self.top
            self.top = self.top.next

            if temp.value < self.minEle:
                x = temp.value
                prev_min_element = 2 * self.minEle - temp.value
                x = (prev_min_element + x) / 2

                self.minEle = 2 * self.minEle - temp.value

                return "{} removed".format(x)

            else:
                return "{} removed".format(temp.value)


new_stack = Stack()

new_stack.push(4)
new_stack.push(5)
new_stack.push(3)
new_stack.push(1)
new_stack.push(4)
new_stack.push(0)
new_stack.pop()
data = new_stack.pop()
print(data)

_, stack = new_stack.__str__()
print(stack)
print(new_stack.minEle)
