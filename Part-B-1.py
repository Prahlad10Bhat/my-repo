#represent binary-each node 3 attributes


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")  # Print data with a space
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")  # Print data with a space

# Create the binary tree
tree = BinaryTree()
tree.root = TreeNode(1)
tree.root.left = TreeNode(2)
tree.root.right = TreeNode(3)
tree.root.left.left = TreeNode(4)
tree.root.left.right = TreeNode(5)

# Perform and print the traversals
print("In-order Traversal:")
tree.in_order_traversal(tree.root)
print()  # Add a newline

print("Post-order Traversal:")
tree.post_order_traversal(tree.root)
print()  # Add a newline
