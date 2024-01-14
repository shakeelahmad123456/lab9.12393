class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_inorder_successor_predecessor(root, key):
    if not root:
        return None, None

    successor = None
    predecessor = None

    while root:
        if key < root.val:
            successor = root
            root = root.left
        elif key > root.val:
            predecessor = root
            root = root.right
        else:
            # Node with key found
            if root.right:
                successor = find_min(root.right)
            if root.left:
                predecessor = find_max(root.left)
            break

    return successor, predecessor

def find_min(node):
    while node.left:
        node = node.left
    return node

def find_max(node):
    while node.right:
        node = node.right
    return node

# Example usage:
# Constructing a sample BST
root = TreeNode(15)
root.left = TreeNode(8)
root.right = TreeNode(20)
root.left.left = TreeNode(5)
root.left.right = TreeNode(10)
root.right.left = TreeNode(17)
root.right.right = TreeNode(25)

# Find successor and predecessor for a node with key 10
successor, predecessor = find_inorder_successor_predecessor(root, 10)

print("In-order successor:", successor.val if successor else None)
print("In-order predecessor:", predecessor.val if predecessor else None)
