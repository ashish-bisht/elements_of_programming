# leetcode 66


def plus_one(nums):
    nums[-1] += 1

    for i in reversed(range(1, len(nums))):
        if nums[i] < 10:
            break

        nums[i] = 0
        nums[i-1] += 1

    if nums[0] == 10:
        nums.append(0)
        nums[0] = 1

    return nums


print(plus_one([1, 3, 9]))

print(plus_one([9, 9, 9]))

print(plus_one([1, 9, 9]))
