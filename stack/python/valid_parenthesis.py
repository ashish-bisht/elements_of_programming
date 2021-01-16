def valid(string):
    paren_dict = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    stack = []
    for ch in string:
        if ch in paren_dict:
            stack.append(ch)
        else:
            if stack and paren_dict[stack[-1]] == ch:
                stack.pop()
            else:
                return False

    return True if not stack else False


print(valid("()[]{}"))
print(valid("()"))
print(valid("(]"))
print(valid("{[]}"))
print(valid("([)]"))
