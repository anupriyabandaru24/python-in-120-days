class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bst_insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = bst_insert(root.left, value)
    else:
        root.right = bst_insert(root.right, value)
    return root


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def bst_min(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.value


# 1. Largest value = the right-most node
def bst_max(root):
    if root is None:
        return None
    current = root
    while current.right:
        current = current.right
    return current.value


# Worked example: k-th smallest via the sorted inorder list (O(n) time and space)
def kth_smallest(root, k):
    values = inorder(root)
    return values[k - 1]


# 2. Is this a valid BST? Its inorder list must never go down.
# (Equal neighbours are allowed, because bst_insert puts equal values on the right.)
def is_valid_bst(root):
    if root is None:
        return True
    values = inorder(root)
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True


if __name__ == "__main__":
    good = None
    for v in [8, 3, 10, 1, 6, 14]:
        good = bst_insert(good, v)

    print(kth_smallest(good, 3))
    print(bst_max(good), bst_max(None), bst_min(good))
    print(is_valid_bst(good))

    bad = TreeNode(5)
    bad.left = TreeNode(3)
    bad.right = TreeNode(8)
    bad.right.left = TreeNode(4)
    bad.right.right = TreeNode(9)
    print(inorder(bad))
    print(is_valid_bst(bad), is_valid_bst(None), is_valid_bst(TreeNode(1)))
