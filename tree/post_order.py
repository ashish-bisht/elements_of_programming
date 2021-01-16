class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder(root):
    stack = []
    res = []
    visited = set()
    while root:
        stack.append(root)
        root = root.left

        while root == None and stack:

            cur = stack.pop()
            if cur.right and cur.val not in visited:
                visited.add(cur.val)
                stack.append(cur)
                root = cur.right
            else:
                res.append(cur.val)
                root = None
    return res


def recursive(root):
    if not root:
        return
    recursive(root.left)
    recursive(root.right)

    print(root.val, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(recursive(root))
print(postorder(root))
