#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_symmetric(root):
    if not root:
        return True

    return helper(root.left, root.right)


def helper(left_side, right_side):
    if not left_side and not right_side:
        return True

    if not left_side and right_side:
        return False

    if not right_side and left_side:
        return False

    if left_side.val != right_side.val:
        return False

    left = helper(left_side.left, right_side.right)
    right = helper(left_side.right, right_side.left)

    return left and right


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)


print(is_symmetric(root))
