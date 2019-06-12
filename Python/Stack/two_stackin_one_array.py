"""
We can also use one array and devide it into two halves, one can be used for stack 1 and other half can be used for
stack 2.

The above approach is inefficient as if you keep pushing elements to only one stack and have not pushed anything in
other stack, then in this case it will give stack OVERFLOW after one point of time.

--------BEST SOLUTION --------

As we have to use onle one array, starting part of the array can be used as stack1 and from the end we can start using
stack2.
i.e =>  stack1.top will at -1 and keep increasing as we push the elements and keep decreasing as we are going to pop.

    => stack2.top will be at len(arr) and keep decreasing as we push the element and decreasing as we pop.
"""


class TwoStack:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, value):
        if self.top1 < self.top2-1:
            self.top1 += 1
            self.arr[self.top1] = value

        else:
            print("Stack 1 overflow.")
            exit(1)

    def push2(self, value):
        if self.top1 < self.top2-1:
            self.top2 -= 1
            self.arr[self.top2] = value

        else:
            print("Stack 2 overflow.")
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            value = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return value

        else:
            print("Stack 1 underflow")
            exit(1)

    def pop2(self):
        if self.top2 < self.size:
            value = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 += 1
            return value

        else:
            print("Stack 2 underflow")
            exit(1)


stack = TwoStack(10)

stack.push1(1)
stack.push1(2)
stack.push2(3)
stack.push2(4)
stack.pop1()
stack.pop2()

print(stack.arr)
