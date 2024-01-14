class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def search_bst(root, target):
    # Base case: if the root is None or the target is found at the root
    if root is None or root.val == target:
        return root

    # If the target is smaller than the root's value, search in the left subtree
    if target < root.val:
        return search_bst(root.left, target)

    # If the target is larger than the root's value, search in the right subtree
    return search_bst(root.right, target)

# Example usage:
# Construct a simple BST:    4
#                           /   \
#                          2     7
#                         / \   / \
#                        1   3 5   8

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(8)

target_value = 5
result = search_bst(root, target_value)
