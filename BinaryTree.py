class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def visit(node):
    # This function can be modified to perform any action on the node
    print(node.value)

def iterative_preorder(root):
    if not root:
        return  # If the tree is empty

    stack = []
    node = root

    while node or stack:
        while node:
            visit(node)
            stack.append(node)
            node = node.left

        node = stack.pop()
        node = node.right


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Performing iterative preorder traversal
iterative_preorder(root)