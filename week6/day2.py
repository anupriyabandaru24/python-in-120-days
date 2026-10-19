class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Search: follow ONE side only, using the BST rule
def bst_contains(root, target):
    if root is None:
        return False
    if target == root.value:
        return True
    if target < root.value:
        return bst_contains(root.left, target)
    return bst_contains(root.right, target)


# 1. Insert (equal values go to the right)
def bst_insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = bst_insert(root.left, value)
    else:
        root.right = bst_insert(root.right, value)
    return root


# 2. Smallest value = the left-most node
def bst_min(root):
    if root is None:
        return None
    current = root
    while current.left:          # fixed: stop ON the last node, not after it
        current = current.left
    return current.value


# 3. Inorder (left, node, right): sorted for a BST
def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


if __name__ == "__main__":
    root = None
    for v in [8, 3, 10, 1, 6, 14]:
        root = bst_insert(root, v)

    print(inorder(root))
    print(bst_min(root), bst_min(None))
    print(bst_contains(root, 6), bst_contains(root, 7))
    bst_insert(root, 7)
    print(inorder(root))
    print(bst_contains(root, 7))
    print(bst_min(TreeNode(5)))
