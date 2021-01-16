def permutations(nums):
    res = []
    helper(nums, [], res)

    return res


def helper(nums, cur, res):
    if not nums:
        res.append(cur)
        return

    for i in range(len(nums)):
        helper(nums[:i] + nums[i+1:], cur + [nums[i]], res)


print(permutations([1, 2, 3]))
