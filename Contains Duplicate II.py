# Given an array of integers and an integer k, return true if and only if there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.



class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        for i in xrange(len(nums)):
            for j in xrange(i+1, i+1 + k):
                if j >= len(nums):
                    return False
                if nums[i] != nums[j]:
                    continue
                else:
                    return True

        return False

