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


def preorder(root):
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


# Lowest common ancestor in a BST: O(h) time, O(1) space
def lca(root, p, q):
    current = root
    while current:
        if p < current.value and q < current.value:
            current = current.left
        elif p > current.value and q > current.value:
            current = current.right
        else:
            return current.value


def merge(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


if __name__ == "__main__":
    root = None
    for v in [4, 2, 6, 1, 3, 5, 7]:
        root = bst_insert(root, v)

    print(preorder(root))
    print(postorder(root))
    print(lca(root, 1, 3), lca(root, 1, 7), lca(root, 5, 7), lca(root, 2, 3))

    print(merge([5, 6], [1, 9]))
    print(merge([3, 1], [2]))   # unsorted input, so the output is NOT sorted

    chain = None
    for v in [1, 2, 3, 4, 5]:
        chain = bst_insert(chain, v)
    print(preorder(chain))      # a chain: every node only has a right child