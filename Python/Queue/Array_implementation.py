class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = capacity-1
        self.size = 0
        self.data = [None]*capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def Enqueue(self, value):
        """
        Function for insertion value in Queue. Insertion is done at the rear end.
        :param value:
        :return:
        """
        if self.isFull():
            return "Queue already full."

        self.rear = (self.rear+1) % self.capacity
        self.data[self.rear] = value
        self.size += 1

    def Dequeue(self):
        """
        Function to delete a value from the queue. Deletion happens at the front end.
        :return:
        """
        if self.isEmpty():
            return "Queue is already empty."

        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1


queue = Queue(10)
print(queue.data, "Initially")
queue.Enqueue(14)
queue.Enqueue(35)
queue.Enqueue(85)
queue.Dequeue()
print(queue.data, "After performing some operations.")
queue.Enqueue(78)
print(queue.data, "One more Insertion")
