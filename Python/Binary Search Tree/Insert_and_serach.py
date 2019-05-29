class Node:
    def __init__(self, key):
        self.value = key
        self.right = None
        self.left = None


def print_inorder(root):
    if root is None:
        return

    print_inorder(root.left)
    print(root.value)
    print_inorder(root.right)


def insert(root, key):
    if root is None:
        return Node(key)

    current = root
    prev = root

    while current:
        if current.value < key:
            prev = current
            current = current.right
        elif current.value > key:
            prev = current
            current = current.left

    if prev.value < key:
        prev.right = Node(key)
    else:
        prev.left = Node(key)

    return root


def insert_recursively(root, key):
    if root is None:
        return Node(key)

    if root.value < key:
        if root.right is None:
            root.right = Node(key)
        else:
            insert_recursively(root.right, key)

    else:
        if root.left is None:
            root.left = Node(key)
        else:
            insert_recursively(root.left, key)


r = Node(8)

#  Iterative insertion.

# insert(r, 3)
# insert(r,10)
# insert(r, 6)


# Insert recursively.

insert_recursively(r, 3)
insert_recursively(r, 10)
insert_recursively(r, 6)
print_inorder(r)
