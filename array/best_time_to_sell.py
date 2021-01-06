nums = [7, 1, 5, 3, 6, 4]

# O(n*n)


def best_time1(nums):
    max_profit = 0
    for i in range(len(nums)):
        cur_profit = 0
        for j in range(i+1, len(nums)):
            cur_profit = nums[j] - nums[i]
            max_profit = max(max_profit, cur_profit)

    return max_profit


print(best_time1(nums))
print(best_time1([7, 6, 4, 3, 1]))


# O(n)

def best_time(nums):
    max_profit = 0
    low = float("inf")

    for price in nums:
        low = min(low, price)
        max_profit = max(max_profit, price - low)
    return max_profit


print(best_time(nums))
print(best_time([7, 6, 4, 3, 1]))
