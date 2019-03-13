from LinkedList import LinkedList

ll = LinkedList()

ll.add_element(1)
ll.add_element(2)
# ll.add_element(4)
ll.add_element(6)
ll.add_element(2)
ll.add_element(5)


def reverse_linkedlist(linkedlist):
    """Reverse the linked lists."""
    prev = None
    current = linkedlist.head
    next = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


def compare_lists(l1, l2):
    """Compare if two linked lists are same or not."""

    print("Compare list 1")
    l1.print_list()
    print("Compare list 2")
    l2.print_list()
    node1 = l1.head
    node2 = l2.head

    while node1 and node2:
        if node1.value != node2.value:
            return False
        node1 = node1.next
        node2 = node2.next

    return True


def is_palindrome(linkedlist):
    """Check if the given linked list is palindrome or not."""
    if not linkedlist.head:
        print("Empty linked list.")

    node1 = linkedlist.head
    node2 = linkedlist.head
    prevnode = None
    midnode = None

    while node1 and node1.next:
        node1 = node1.next.next
        prevnode = node2
        node2 = node2.next

    if not node1:
        midnode = node2
    else:
        midnode = node2.next

    prevnode.next = None

    list2 = LinkedList()
    list2.head = midnode

    print("Original ")
    linkedlist.print_list()

    print("2nd Half")
    list2.print_list()

    revlinkedlist = LinkedList()

    revlinkedlist.head = reverse_linkedlist(list2)

    print("Reversed 2nd half")
    revlinkedlist.print_list()

    result = compare_lists(linkedlist, revlinkedlist)

    print("Given linkedlist is palindrome:- ", result)


is_palindrome(ll)
