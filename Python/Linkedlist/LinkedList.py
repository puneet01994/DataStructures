from base_linkedlist import Node


class LinkedList:

    def __init__(self, head=None):
        self.head = head

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

    def remove_from_end(self):
        """Remove the last element of the linked list."""
        head1 = self.head

        while head1.next.next is not None:
            head1 = head1.next

        head1.next = None

    def remove_element_at_given_position(self, pos):
        """Removes an element from a linked list at a given position. (Index starts from 0.)"""
        if self.head is None:
            print("Can not removes Element as the linked list provided is empty.")
            return

        head1 = self.head

        if pos == 0:
            self.head = head1.next
            head1 = None
            return

        for i in range(0, pos-1):
            head1 = head1.next
            if head1.next is None:
                break

        if head1.next is None:
            print("Please try with some smaller number.")
            return

        if head1.next.next is not None:
            head1.next = head1.next.next
        else:
            head1.next = None

    def remove_element(self, num):
        """Removes an element from the linked list."""
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.value == num:
            self.head = self.head.next
            print("Deleted the element.")
            return

        head1 = self.head
        prev = None

        while head1 is not None:
            if head1.value == num:
                break
            prev = head1
            head1 = head1.next

        if head1 is None:
            print("Value not found.")
            return

        prev.next = head1.next
        print("Deleted the given number.")

    def get_count(self, head1):
        """Recursive function to find length of a linked list."""
        if not head1:
            return 0

        return 1 + self.get_count(head1.next)

    def length_of_linked_list(self):
        """Length of the linked list."""
        return self.get_count(self.head)


print("******************Cases to add elements at the end of the linked list.******************")

l1 = LinkedList()

l1.add_element(2)
l1.add_element(3)
l1.add_element(4)
l1.add_element(5)

l1.print_list()

print("******************Cases to add elements at a given position.******************")

l1.add_element_at_given_position(9, 4)

l1.print_list()

print("******************Cases to remove elements from the end.******************")

l1.remove_from_end()

l1.print_list()

leng = l1.length_of_linked_list()
print("Length of the linked list is {0}".format(leng))


print("******************Cases to remove elements from the given position.******************")

l1.remove_element_at_given_position(2)

l1.print_list()

# l1.remove_element_at_given_position(0)
# l1.print_list()
#
# l1.remove_element_at_given_position(0)
# l1.print_list()
#
# l1.remove_element_at_given_position(0)
# l1.print_list()

# l1.remove_element_at_given_position(7)

leng = l1.length_of_linked_list()
print("Length of the linked list is {0}".format(leng))

print("******************Cases to remove given element.******************")

l1.remove_element(3)

l1.remove_element(2)

l1.remove_element(6)
l1.print_list()