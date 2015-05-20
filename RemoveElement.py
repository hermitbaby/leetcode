# Given an array and a value, remove all instances of that value in place and return the new length.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.


class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        """
        Two pointers
        1 change num[i]= num[i+1], if num[i] == val
        2 or change num[i] with the last element in list
        """
        i, j = 0, 0
        if len(nums) == 0:
            return 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        # print nums
        return j


s = Solution()
print s.removeElement([1,2,3,4,5,3,6,7], 3)

