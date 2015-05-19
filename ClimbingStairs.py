# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        """
        Simplest DP problem
        In order to climb the nth stair, from the n-2 th stair to climb 2, or from the n-1 th stair to climb 1
        dp[n] = dp[n-2] + dp[n-1]

        """
        if n in set([0, 1, 2]):
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in xrange(3, len(dp)):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]


s = Solution()
print s.climbStairs(4)
