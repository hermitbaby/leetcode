# Given a set of distinct integers, nums, return all possible subsets.
#
# Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]



class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        def dfs(depth, start, valuelist):
            print '\t\t' * depth, 'start:', start, 'valuelist', valuelist, 'depth:', depth
            res.append(valuelist)
            # if depth == len(nums):
            #     return

            for i in range(start, len(nums)):
                dfs(depth+1, i+1, valuelist+[nums[i]])

        nums.sort()
        res = []
        dfs(0, 0, [])
        return res


    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        def dfs(depth, start, valuelist):
            # print 'depth:', depth, 'start:', start, 'valuelist', valuelist
            if valuelist not in res:
                res.append(valuelist)
            if depth == len(nums):
                return

            for i in range(start, len(nums)):
                dfs(depth+1, i+1, valuelist+[nums[i]])

        nums.sort()
        res = []
        dfs(0, 0, [])
        return res




s = Solution()
print s.subsets([1, 2, 3])