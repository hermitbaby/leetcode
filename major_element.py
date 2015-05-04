# Given an array of size n, find the majority element. The majority element is the element that appears more than  _n/2 times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        # other approachs
        # at least 7 ways
        # 0 hashmap
        # 1 brutal
        # 2 sort
        # 3 divide & conque
        # 4 elect
        # 5 bit
        count = {}
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
                if count[num] > len(nums)/2:
                    return num

    def majorityElement1(self, nums):
        # major element must be in the middle index
        # directly return nums[n/2]
        sort_nums = sorted(nums)
        count = 1
        for i in xrange(1, len(sort_nums)):
            if sort_nums[i] == sort_nums[i-1]:
                count += 1
                if count > len(nums)/2:
                    return sort_nums[i]


s = Solution()
# print s.majorityElement([1, 2, 3, 4, 5, 1, 1, 1, 1])
print s.majorityElement1([1, 2, 3, 4, 5, 1, 1, 1, 1])




