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
# -*- coding: utf-8 -*-
# from rcviz import callgraph, viz


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}

    def subsets170415(self, nums):

        res = []

        """
        def recurse(rest_elements, set_so_far, start):
            if level == len(nums):
                return

            for idx in xrange(start, rest_elements):
                rest = rest_elements[:idx] + rest_elements[idx+1:]
                cur = rest_elements[idx]
                recurse(rest, set_so_far + [cur], start+1)

        """

        def recurse(start, valuelist):
            res.append(valuelist)

            for idx in xrange(start, len(nums)):
                recurse(idx + 1, valuelist + [nums[idx]])   # !! not start+1

        recurse(0, [])

        return res


    def subsets_Dup170415(self, nums):

        res = []

        def recurse(start, valuelist):
            if valuelist not in res:
                res.append(valuelist)

            for idx in xrange(start, len(nums)):
                recurse(idx + 1, valuelist + [nums[idx]])   # !! not start+1

        recurse(0, [])

        return res






    def subsets(self, nums):


        def dfs(depth, start, valuelist):
            # print '\t\t' * depth, 'start:', start, 'valuelist', valuelist, 'depth:', depth
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
# print s.subsets170415([1, 2, 3])
# print s.subsets([1, 2, 3])

print s.subsets_Dup170415([1, 2, 2])
print s.subsetsWithDup([1, 2, 2])

"""
def subsets(nums):

    nums.sort()
    res = []
    dfs(0, 0, [])

    return res

res = []
nums = [1, 2, 3]

@viz
def dfs(start, valuelist):

    res.append(valuelist)
    dfs.track(start=start)
    # if depth == len(nums):
    #     return

    for i in range(start, len(nums)):
        dfs( i + 1, valuelist + [nums[i]])

dfs(0, [])
callgraph.render("pic/subset.svg")

"""