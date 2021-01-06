# leectode 75..
# Time O(n) space O(1)


def sort_colors(nums):

    left = zero = 0
    right = len(nums)-1

    while left <= right:

        if nums[left] == 0:
            nums[left], nums[zero] = nums[zero], nums[left]
            left += 1
            zero += 1

        elif nums[left] == 2:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1

        else:
            left += 1

    return nums


print(sort_colors([2, 0, 2, 0, 1, 2, 0, 0, 1, 1, 1, 0]))
print(sort_colors([2, 0, 1]))
