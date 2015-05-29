# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.



class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0

        pos_max, neg_min = [nums[0]], [nums[0]]
        for i in xrange(1, len(nums)):
            pos_top = pos_max[-1]
            neg_top = neg_min[-1]

            pos_max.append(max(nums[i], nums[i] * pos_top, nums[i] * neg_top))
            neg_min.append(min(nums[i], nums[i] * pos_top, nums[i] * neg_top))
        return max(pos_max)
