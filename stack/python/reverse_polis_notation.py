def revrese_polis_notation(tokens):
    valid_tokens = {"+", "-", "*", "/"}
    stack = []
    for token in tokens:
        if token in valid_tokens:
            num2 = stack.pop()
            num1 = stack.pop()

            temp = helper(num1, num2, token)
            stack.append(temp)
        else:
            stack.append(int(token))
    return stack[0]


def helper(num1, num2, token):
    if token == "+":
        return num1 + num2
    if token == "-":
        return num1 - num2

    if token == "*":
        return num1*num2

    if token == "/":
        return int(float(num1) / num2)


print(revrese_polis_notation(["2", "1", "+", "3", "*"]))
print(revrese_polis_notation(["4", "13", "5", "/", "+"]))
print(revrese_polis_notation(
    ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

print(revrese_polis_notation(["4", "3", "-"]
                             ))
