from base_linkedlist import Node
from LinkedList import LinkedList

ll = LinkedList()

ll.add_element(1)
ll.add_element(2)
ll.add_element(3)
ll.add_element(4)
ll.add_element(5)


def reverse_linkedlist(l1):
    """Reverse the given linkedlist."""
    prev = Node()
    current = l1.head
    next = Node()

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


print("******************Reverse of the Linked List.******************")

ll.print_list()

l2 = reverse_linkedlist(ll)

rl = LinkedList()
rl.head = l2

rl.print_list()
