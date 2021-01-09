def del_duplicates(nums):
    index = 1
    last_num = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != last_num:
            nums[index] = nums[i]
            last_num = nums[i]
            index += 1
    return nums


print(del_duplicates([1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 6, 7, 7]))
print(del_duplicates([1, 1, 2, 2, 3, 5]))
n
