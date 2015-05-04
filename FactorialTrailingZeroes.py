# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.


class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        div = 5
        count_5 = 0
        while n >= div:
            count_5 += n / div
            div *= 5
        return count_5


s = Solution()
print s.trailingZeroes(1000)

