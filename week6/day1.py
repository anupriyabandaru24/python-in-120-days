from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 1. Sum of all values
def sum_values(root):
    if root is None:
        return 0
    return root.value + sum_values(root.left) + sum_values(root.right)


# 2. Preorder: node, left, right
def preorder(root):
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


# 3. Postorder: left, right, node
def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


# 4. Count leaves
def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


# 5. Height (empty tree = 0)
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


# 6. Is the target in the tree?
def contains(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    return contains(root.left, target) or contains(root.right, target)


# 7. Largest value (None for an empty tree)
def max_value(root):
    if root is None:
        return None

    def helper(node):
        if node is None:
            return float("-inf")
        return max(node.value, helper(node.left), helper(node.right))

    return helper(root)


# 8. Mirror the tree
def invert(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    invert(root.left)
    invert(root.right)
    return root


# 9. Level-order (BFS)
def level_order(root):
    if root is None:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


# 10. Root-to-leaf path with this sum?
def has_path_sum(root, target):
    if root is None:
        return False
    remaining = target - root.value
    if root.left is None and root.right is None:
        return remaining == 0
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(sum_values(root), sum_values(None))
    print(preorder(root), postorder(root))
    print(count_leaves(root), height(root), height(None))
    print(contains(root, 5), contains(root, 3), contains(root, 9), contains(None, 1))
    print(max_value(root), max_value(None))
    print(level_order(root), level_order(None))
    print([has_path_sum(root, t) for t in (7, 4, 8, 5)], has_path_sum(None, 0))

    # extra shapes: one-child tree and a chain
    one = TreeNode(1)
    one.left = TreeNode(2)
    print(has_path_sum(one, 1), has_path_sum(one, 3))
    chain = TreeNode(1)
    chain.left = TreeNode(2)
    chain.left.left = TreeNode(3)
    print(count_leaves(chain), height(chain))

    # invert last, because it changes the tree
    print(preorder(invert(root)), invert(None))
