#
# A peak element is an element that is greater than its neighbors.
#
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
#
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
#
# You may imagine that num[-1] = num[n] = -∞.
#
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
#
# Note:
# Your solution should be in logarithmic complexity.


class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        n = len(nums)
        for i in xrange(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        if nums[0] > nums[1]:
            return 0
        if nums[n-2] < nums[n-1]:
            return n-1


    def findPeakElement2(self, nums):
        def search(nums, s, e):
            if s == e:
                return s
            if s + 1 == e:
                return[s, e][nums[s] < nums[e]]

            mid = (s + e) / 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid-1]:
                return search(nums, s, mid-1)
            else:
                return search(nums, mid+1, e)


        n = len(nums)
        res = search(nums, 0, n-1)
        return res


