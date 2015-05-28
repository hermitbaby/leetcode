# Given an array of integers, every element appears three times except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        dict = {}

        for x in nums:
            if x not in dict:
                dict[x] = 1
            else:
                dict[x] += 1

        for key in dict:
            if dict[key] == 1:
                return key