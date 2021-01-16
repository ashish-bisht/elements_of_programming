def generateparenthese(n):
    res = []

    helper(n, n, n, '', res)
    return res


def helper(n, left_bracket, right_bracket, cur, res):

    if left_bracket < 0 or right_bracket < 0:
        return

    if left_bracket > right_bracket:
        return

    if n*2 == len(cur):
        res.append(cur)
        return

    helper(n, left_bracket-1, right_bracket, cur + "(", res)
    helper(n, left_bracket, right_bracket-1, cur + ")", res)


print(generateparenthese(3))
print(generateparenthese(2))
