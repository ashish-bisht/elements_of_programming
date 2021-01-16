def building_facing_sun(nums):
    max_so_far = nums[0]
    ans = 1
    for num in nums[1:]:
        if num > max_so_far:
            ans += 1
            max_so_far = num

    return ans


print(building_facing_sun([7, 4, 8, 2, 9]))
print(building_facing_sun([2, 3, 4, 5]))
