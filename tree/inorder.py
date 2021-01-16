class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    stack = []
    res = []

    while root:
        stack.append(root)
        root = root.left

        while root == None and stack:
            cur = stack.pop()
            res.append(cur.val)
            root = cur.right

    return res


def recursive(root):
    if not root:
        return

    recursive(root.left)
    print(root.val)
    recursive(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


print(recursive(root))
print(inorder(root))
