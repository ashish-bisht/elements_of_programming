# Kadence Algorithm, O(n), space O(n)

def max_subarray(nums):
    dp = [0] * len(nums)

    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1]+nums[i], nums[i])
    return max(dp)


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
