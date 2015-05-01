# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}

    # brutal force search
    def twoSum0(self, nums, target):
        # xrange(4, 4)? left< right? usage
        for i in xrange(0, len(nums)):
            for j in xrange(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    i += 1
                    j += 1
                    if i < j:
                        return [i, j]
                    else:
                        return [j, i]
        return []

    # hash
    def twoSum(self, nums, target):
        dict = {}
        for i in xrange(len(nums)):
            # if duplicate num, don't put in dict
            if nums[i] not in dict:
                dict[nums[i]] = i
            find_for = target - nums[i]
            if find_for in dict:
                a = dict[find_for]+1
                b = i+1
                if a != b:
                    return [a,b] if a<b else [b,a]
        return []



s= Solution()
print s.twoSum(nums=[2, 7, 11, 15], target=22)
print s.twoSum(nums=[0, 4, 3, 0], target=0)
# 22