matrix = [[1, 0, 0, 0],
          [1, 1, 0, 1],
          [1, 1, 0, 0],
          [0, 1, 1, 1]]


def rat_in_maze(matrix):
    res = []
    helper(matrix, 0, 0, [], res)
    return res


def helper(matrix, row, col, cur, res):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == 0:
        return

    if row == len(matrix)-1 and col == len(matrix[0])-1:
        res.append(cur)
        return

    temp = matrix[row][col]

    matrix[row][col] = 0

    helper(matrix, row-1, col, cur + ["U"], res)
    helper(matrix, row+1, col, cur + ["D"], res)
    helper(matrix, row, col-1, cur + ["L"], res)
    helper(matrix, row, col+1, cur + ["R"], res)

    matrix[row][col] = temp


print(rat_in_maze(matrix))
