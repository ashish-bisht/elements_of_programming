# leetcode 55
# Time O(n) space O(1)

def can_reach(nums):
    if not nums:
        return False

    max_reach = nums[0]

    for i in range(len(nums)):
        cur_reach = nums[i]+i
        max_reach = max(max_reach, cur_reach)

        if i >= max_reach and i != len(nums)-1:
            return False
    return True


print(can_reach([3, 2, 1, 0, 4]))
print(can_reach([2, 3, 1, 1, 4]))
print(can_reach([3, 2, 1, 1, 4]))
