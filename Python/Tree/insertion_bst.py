from base_tree import Node


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert_in_bst(self, value):
        n = Node(value)
        if self.root is None:
            self.root = n
            return

        parent = None
        current = self.root

        while current is not None:
            parent = current
            if current.data < value:
                current = current.right
            else:
                current = current.left

        if parent.data < value:
            parent.right = n
        else:
            parent.left = n

        return

    def preorder_traversal(self, root):
        if root:
            print(root.data, "-->", end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
            print(root.data, "-->", end=" ")

    def inorder_traversal(self, root):
        if root:
            self.preorder_traversal(root.left)
            print(root.data, "-->", end=" ")
            self.preorder_traversal(root.right)


tree = BST()

tree.insert_in_bst(4)
tree.insert_in_bst(6)
tree.insert_in_bst(3)
tree.insert_in_bst(9)
tree.insert_in_bst(2)
print()
print("Pre Order traversal")
tree.preorder_traversal(tree.root)
print()
print("Post order traversal")
tree.postorder_traversal(tree.root)
print()
print("Inorder traversal")
tree.inorder_traversal(tree.root)
