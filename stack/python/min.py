class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if self.min_stack and self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self):
        if self.min_stack:
            self.min_stack.pop()
        if self.stack:
            return self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def get_min(self):
        if self.min_stack:

            return self.min_stack[-1]


stack = Stack()
print(stack.top())
print(stack.push(1))

print(stack.top())

print(stack.push(2))

print(stack.top())
