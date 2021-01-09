class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowest_common_ans(root, p, q):
    if not root:
        return None

    if root.val == p or root.val == q:
        return root.val

    left = lowest_common_ans(root.left, p, q)
    right = lowest_common_ans(root.right, p, q)

    if left and right:
        return root.val

    return left if not right else right


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("LCA(4,5) = ", lowest_common_ans(root, 4, 5))
print("LCA(4,6) = ", lowest_common_ans(root, 4, 6))
print("LCA(3,4) = ", lowest_common_ans(root, 3, 4))
print("LCA(2,4) = ", lowest_common_ans(root, 2, 4))
