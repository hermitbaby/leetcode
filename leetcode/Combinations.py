# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# -*- coding: utf-8 -*-
# from rcviz import callgraph, viz

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine_070415(self, n, k):

        res = []

        def recurse(start, valuelist):
            if len(valuelist) == k:
                res.append(valuelist)
                return

            for idx in xrange(start, n+1):
                recurse(idx+1, valuelist + [idx])

        recurse(1, [])
        return res







    def combine(self, n, k):
        def dfs(start, valuelist, depth):

            if depth == k:      # self.count == k:
                ret.append(valuelist)
                return
            for i in range(start, n + 1):

                # Notice: valuelist is before [i]; old element + new element
                dfs(i + 1, valuelist + [i], depth + 1)


        ret = []

        dfs(1, [], 0)
        return ret


s = Solution()
print s.combine(4, 3)
print s.combine_070415(4, 3)

"""
n, k = 4, 2
ret = []

@viz
def dfs(start, valuelist):

    if len(valuelist) == k:
        ret.append(valuelist)
        return
    for i in range(start, n + 1):
        dfs(i + 1, valuelist + [i])

dfs(1, [])
callgraph.render("pic/combination.svg")
"""