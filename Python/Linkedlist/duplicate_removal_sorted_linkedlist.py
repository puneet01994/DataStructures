from LinkedList import LinkedList

linkedlist = LinkedList()

linkedlist.add_element(1)
linkedlist.add_element(2)
linkedlist.add_element(3)
linkedlist.add_element(3)
linkedlist.add_element(4)
linkedlist.add_element(6)
linkedlist.add_element(6)


def remove_duplicate_from_sorted_linkedlist(linkedlist):
    if not linkedlist.head:
        print("Linked list is empty.")

    current = linkedlist.head

    while current and current.next:
        if current.value == current.next.value:
            temp = current.next
            if current.next.next:
                current.next = temp.next
            else:
                current.next = None
            temp.next = None

        current = current.next

    return linkedlist


unique_list = remove_duplicate_from_sorted_linkedlist(linkedlist)
print("Linked list after removal of duplicates.")
unique_list.print_list()
