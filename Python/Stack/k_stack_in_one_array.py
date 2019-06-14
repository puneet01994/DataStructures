class KStack:
    def __init__(self, k, n):
        self.arr = [None for i in range(n)]
        self.top = [-1 for i in range(k)]
        self.next = [i+1 for i in range(n)]
        self.next[n-1] = -1

        self.curr = 0

    def is_full(self):
        if self.curr == -1:
            return True

        return False

    def is_empty(self,sn):
        if self.top[sn] == -1:
            return True

        return False

    def push(self, value, sn):
        if self.is_full():
            return "Stack Overflow."

        insert_at = self.curr

        self.arr[insert_at] = value

        self.curr = self.next[self.curr]
        self.next[insert_at] = self.top[sn]
        self.top[sn] = insert_at

    def pop(self, sn):
        if self.is_empty(sn):
            return "Empty stack."

        top_idx = self.top[sn]
        self.arr[top_idx] = None

        self.top[sn] = self.next[top_idx]
        self.next[top_idx] = self.curr
        self.curr = top_idx


kstack = KStack(3, 10)
print(kstack.pop(2))
kstack.push(17, 2)
kstack.push(43, 1)
kstack.push(28, 2)
kstack.push(42, 0)
kstack.push(35, 2)

print(kstack.arr)
print(kstack.top)
print(kstack.next)
