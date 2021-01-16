def subsets(nums):
    res = []
    helper(nums, [], res)
    return res


def helper(nums, cur, res):

    res.append(cur)

    for i in range(len(nums)):
        helper(nums[i+1:], cur + [nums[i]], res)


print(subsets([1, 2, 3]))
