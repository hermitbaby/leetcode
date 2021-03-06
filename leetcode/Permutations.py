# Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

# -*- coding: utf-8 -*-
# from rcviz import callgraph, viz


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute_070415(self, nums):

        res = []

        def recurse(rest_nums, valuelist):
            if len(valuelist) == len(nums):
                res.append(valuelist)

            for idx in range(len(rest_nums)):
                rest = rest_nums[:idx] + rest_nums[idx+1:]
                recurse(rest, valuelist+[rest_nums[idx]])

        recurse(nums, [])
        return res

    def permuteDup_070415(self, nums):

        res = []

        def recurse(rest_nums, valuelist):
            if len(valuelist) == len(nums) and valuelist not in res:
                res.append(valuelist)

            for idx in range(len(rest_nums)):
                rest = rest_nums[:idx] + rest_nums[idx+1:]
                recurse(rest, valuelist+[rest_nums[idx]])

        recurse(nums, [])
        return res

    def permuteDup2_070415(self, nums):

        res = []

        def recurse(rest_nums, valuelist):
            if len(valuelist) == len(nums):
                res.append(valuelist)

            pre = None
            for idx in range(len(rest_nums)):
                rest = rest_nums[:idx] + rest_nums[idx+1:]
                if rest_nums[idx] != pre:
                    recurse(rest, valuelist+[rest_nums[idx]])
                    pre = rest_nums[idx]

        recurse(nums, [])
        return res


    def permute(self, nums):


        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        res = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                print 'i=', i, 'j=', j, 'nums[:i] + nums[i+1:] =', nums[:i] + nums[i+1:]
                res.append([nums[i]] + j)
                print [nums[i]] + j, res

        return res


    def permute2(self, num):
        """
        1 normal dfs, no fancy stuff
        2
        """
        def dfs(node, rest_list, res, counter):
            print "\t\t" * counter, 'depth=', counter, '|node=', node, '| rest_list=', rest_list, '| res=', res
            if rest_list == []:
                res.append(node)
            else:
                for i in range(len(rest_list)):
                    # print 'i=', i
                    # rest_list[:i] + rest_list[i+1:] means
                    #    in rest_list, excludes rest_list[i]

                    # new_node_list = node+[rest_list[i]]
                    # print 'error: i', i, rest_list
                    # node.append(rest_list[i])
                    new_node_list = []
                    new_node_list[:] = node[:]
                    new_node_list.append(rest_list[i])

                    # new_rest_list = rest_list[:i] + rest_list[i+1:]
                    # rest_list.pop(i)
                    # print new_rest_list
                    new_rest_list = []
                    # parameter name problem
                    # print 'should change:', rest_list
                    new_rest_list[:] = rest_list[:]
                    new_rest_list.pop(i)
                    # node+[rest_list[i]], rest_list[:i] + rest_list[i+1:]
                    dfs(new_node_list, new_rest_list, res, counter+1)

        # mutable object(list) is passed by ref, in python
        # int is passed by value
        counter = 0

        res = []
        dfs([], num, res, counter)
        # print counter
        return res


    def permuteUnique(self, num):
        def dfs(node, rest_list):

            if rest_list == []:
                res.append(node)
            else:
                prev = None
                for i in range(len(rest_list)):
                    # print 'i=', i
                    # rest_list[:i] + rest_list[i+1:] means
                    #    in rest_list, excludes rest_list[i]
                    if rest_list[i] != prev:
                        dfs(node+[rest_list[i]], rest_list[:i] + rest_list[i+1:])
                        prev = rest_list[i]

        # mutable object(list) is passed by ref, in python
        # int is passed by value
        counter = 0

        res = []
        s_num = sorted(num)
        dfs([], s_num)
        # print counter
        return res




s = Solution()
# print s.permute([1, 2, 3])
print s.permute_070415([1, 2, 3])
print s.permuteDup_070415([1, 1, 2])
print s.permuteDup2_070415([1, 1, 2])

# num = []
# i = 10, Mem = 400MB
# i = 11, Mem = 6GB
# import sys
# max recursion level is 1000
# print sys.getrecursionlimit()

# for i in xrange(1, 4):
#     num.append(i)
# print s.permute2(num)

# print (s.permuteUnique([1,1,2,3]))
# print (s.permute2([1, 2, 3]))


"""

res = []
num = [1, 2, 3]


@viz
def dfs(node, rest_list):
    if rest_list == []:
        res.append(node)
    else:
        for i in range(len(rest_list)):

            # node+[rest_list[i]], rest_list[:i] + rest_list[i+1:]
            dfs(node+[rest_list[i]], rest_list[:i] + rest_list[i+1:])

# dfs([], num)
# callgraph.render("pic/permutation.svg")



res2 = []
num2 = [1, 1, 2]

@viz
def dfs_uniq(node, rest_list):
    if rest_list == []:
        res2.append(node)
    else:
        prev = None
        for i in range(len(rest_list)):
            # print 'i=', i
            # rest_list[:i] + rest_list[i+1:] means
            #    in rest_list, excludes rest_list[i]
            if rest_list[i] != prev:
                dfs_uniq(node + [rest_list[i]], rest_list[:i] + rest_list[i + 1:])
                prev = rest_list[i]

dfs_uniq([], num2)
callgraph.render("pic/permutation_uniq.svg")

"""