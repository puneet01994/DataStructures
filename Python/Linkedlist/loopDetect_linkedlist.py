from LinkedList import LinkedList
from base_linkedlist import Node

n = Node(1)

l1 = LinkedList()
#
l1.head = n

l1.add_element(2)
l1.add_element(3)
l1.add_element(4)
l1.add_element(5)

l1.head.next.next.next = l1.head


def detect_loop(ll):
    if l1.head is None:
        print("Given linked list is empty,")
        return
    n1 = ll.head
    n2 = ll.head

    while n2 and n1 and n1.next:

        n1 = n1.next.next
        n2 = n2.next

        if n1 == n2:
            print("Loop detected.")
            return

    print("No loop found.")


print("******************Loop detection in Linked List.******************")
detect_loop(l1)

print("******************Length of the loop in Linked List.******************")


def length_of_loop(ll):
    n1 = ll.head
    n2 = ll.head

    while n1 and n2 and n2.next:
        n1 = n1.next
        n2 = n2.next.next

        if n1 == n2:
            break

    count = 1
    n2 = n2.next

    while n1 != n2:
        n2 = n2.next
        count += 1

    print("Length of the loop in the given linked list is ", count+1)


length_of_loop(l1)
