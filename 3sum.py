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
            # set different target
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

s = Solution()
print s.threeSum([-1, 0, 1, 2, -1, -4])


