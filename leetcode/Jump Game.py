# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return true.
#
# A = [3,2,1,0,4], return false.



class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        # find the max possible steps in each position
        # step = max(nums[i-1]-1, nums[i)
        step = nums[0]

        for i in xrange(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True
