def sell_stock(nums):
    max_profit = 0
    for i in range(1, len(nums)):
        if nums[i-1] < nums[i]:
            max_profit += nums[i] - nums[i-1]
    return max_profit


print(sell_stock([7, 1, 5, 3, 6, 4]))
