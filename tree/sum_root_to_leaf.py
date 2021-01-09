#    1
#    / \
#   2   3


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_root_to_leaf(root):
    res = []

    helper(root, 0, res)
    print(res)
    return sum(res)


def helper(root, cur, res):
    if not root:
        return 0
    cur = cur * 10 + root.val
    if not root.left and not root.right:
        res.append(cur)
        return

    helper(root.left, cur, res)
    helper(root.right, cur, res)


root = Node(1)
root.left = Node(2)
root.right = Node(3)

print(sum_root_to_leaf(root))
