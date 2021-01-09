#    1
#    / \
#   2   3


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def has_path_sum(root, sum):
    return helper(root, sum, 0)


def helper(root, sum, cur):
    if not root and sum == cur:
        return True

    if not root and sum != cur:
        return False

    cur = cur*10 + root.val

    left = helper(root.left, sum, cur)
    right = helper(root.right, sum, cur)

    return left or right


root = Node(1)
root.left = Node(2)
root.right = Node(3)

print(has_path_sum(root, 12))
print(has_path_sum(root, 13))
print(has_path_sum(root, 15))
