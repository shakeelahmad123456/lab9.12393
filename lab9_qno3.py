class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_max_bst(root):
    if root is None:
        return None, None
    
    # Traverse to the leftmost node to find the minimum value
    while root.left is not None:
        root = root.left
    minimum = root.value

    # Traverse to the rightmost node to find the maximum value
    while root.right is not None:
        root = root.right
    maximum = root.value

    return minimum, maximum

# Example usage:
# Construct a simple BST:
#       5
#      / \
#     3   8
#    / \
#   1   4
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)

min_value, max_value = find_min_max_bst(root)

print(f"Minimum value in BST: {min_value}")
print(f"Maximum value in BST: {max_value}")
