# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        """
        # 1 brutal force
        # 2 DP

        DP vs Greedy vs divide&conque
        """
        size = len(nums)
        if size == 0:
            return 0
        dp = [0] * size
        # if nums is []?
        dp[0] = nums[0]
        if size == 1:
            return dp[0]
        dp[1] = nums[1] if nums[1] > nums[0] else nums[0]
        if size == 2:
            return dp[1]
        for i in xrange(2, size):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[size-1]


s = Solution()
nums = [10, 5, 1, 8]
nums1 = [0]
print s.rob(nums1)


