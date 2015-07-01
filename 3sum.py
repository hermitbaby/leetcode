# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
# Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <=  c)
# The solution set must not contain duplicate triplets.
#     For example, given array S = {-1 0 1 2 -1 -4},
#
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        result = []
        s_num = sorted(num)
        for i in xrange(len(s_num)-2):
            # set different target: skip duplicated target
            # after sorting, if s_num[i] == s_num[i-1], the result will be the same
            if i == 0 or s_num[i] > s_num[i-1]:
                target = -s_num[i]
                left = i + 1
                right = len(s_num) - 1

                while left < right:
                    if s_num[left] + s_num[right] == target:
                        item = []
                        item.append(s_num[i])
                        item.append(s_num[left])
                        item.append(s_num[right])
                        result.append(item)
                        left += 1
                        right -= 1
                        # skip the same tuple result
                        # left & left-1, not left & left+1, cur index campared with last index
                        while left < right and s_num[left] == s_num[left-1]:
                            left += 1
                        while left < right and s_num[right] == s_num[right+1]:
                            right -= 1

                    elif s_num[left] + s_num[right] < target:
                        left += 1
                    elif s_num[left] + s_num[right] > target:
                        right -= 1
        return result


    def threeSum1(self, num):
        # 1 brutal force way
        # 2 reuse twoSum way
        res = []
        for i in xrange(len(num)-2):
            for j in xrange(i+1, len(num)-1):
                for k in xrange(j+1, len(num)):
                    if num[i] + num[j] + num[k] == 0:
                        res.append([num[i], num[j], num[k]])

        # remove duplicated result by using tuple and set
        res2 = set()
        for arr in res:
            t = tuple(sorted(arr))
            res2.add(t)
        # print list(res2)

        res3 = []
        for t in res2:
            res3.append(list(t))
        # print res3

        return (res3)


    def fourSum(self, nums, target):
        # 1 brutal force
        # 2 using 3 sum result
        res = []
        for i in xrange(len(nums)-3):
            for j in xrange(i+1, len(nums)-2):
                for k in xrange(j+1, len(nums)-1):
                    for l in xrange(k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            res.append(sorted([nums[i], nums[j], nums[k], nums[l] ]))
        return res




s = Solution()
# print s.threeSum1([-1, 0, 1, 2, -1, -4])
# print s.threeSum1([-1, 0, 1, 2, -1, -4])
num = [1, 0, -1, 0, -2, 2,]
print s.fourSum(num, 0)
