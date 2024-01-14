class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    """
    Function to find the k-th smallest element in a BST.

    Parameters:
    - root: The root of the BST.
    - k: The position of the element to find.

    Returns:
    - The k-th smallest element.
    """
    # Helper function for in-order traversal
    def in_order_traversal(node):
        if not node:
            return []
        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

    # Perform in-order traversal
    elements = in_order_traversal(root)

    # Check if k is within the valid range
    if 1 <= k <= len(elements):
        return elements[k - 1]
    else:
        return None

# Example usage:
# Construct a sample BST
#        3
#       
