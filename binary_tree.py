class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Construct the binary tree
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(40)
root.left.right = TreeNode(20)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

def in_order_traversal(node, result=None):
    if result is None:
        result = []
    if node:
        in_order_traversal(node.left, result)
        result.append(node.value)
        in_order_traversal(node.right, result)
    return result

def pre_order_traversal(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        pre_order_traversal(node.left, result)
        pre_order_traversal(node.right, result)
    return result

def post_order_traversal(node, result=None):
    if result is None:
        result = []
    if node:
        post_order_traversal(node.left, result)
        post_order_traversal(node.right, result)
        result.append(node.value)
    return result

# Testing the traversal functions
print("In-order Traversal:", in_order_traversal(root))       # Expected: [40, 30, 20, 50, 60, 70, 80]
print("Pre-order Traversal:", pre_order_traversal(root))     # Expected: [50, 30, 40, 20, 70, 60, 80]
print("Post-order Traversal:", post_order_traversal(root))   # Expected: [40, 20, 30, 60, 80, 70, 50]
