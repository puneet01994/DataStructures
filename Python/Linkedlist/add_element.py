from base_linkedList import Node


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def add_element(self, value):
        """Add an element in the end of the linked list."""
        new_node = Node(value)
        head1 = self.head
        if head1 is not None:
            while head1.next is not None:
                head1 = head1.next

            head1.next = new_node

        else:
            self.head = new_node

    def print_list(self):
        """Print the complete linked list."""
        if self.head is None:
            print("This Linked list is empty.")

        else:
            head1 = self.head
            while head1.next is not None:
                print(head1.value, "-->", end=" ")
                head1 = head1.next
            print(head1.value)

    def add_element_at_given_position(self, value, pos):
        """Add element at the given position in the linked list, Index starts from 0."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        head1 = self.head
        size = 1
        for i in range(1, pos):
            if head1.next is not None:
                head1 = head1.next
                size += 1

        if pos <= size:
            new_node.next = head1.next
            head1.next = new_node

        else:
            print("Given position does not exists.")


l1 = LinkedList()

l1.add_element(2)
l1.add_element(3)
l1.add_element(4)
l1.add_element(5)

l1.print_list()

print("******************Cases to add elements at a given position.******************")

l1.add_element_at_given_position(9, 4)

l1.print_list()