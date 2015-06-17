# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        tmp = [str(num) for num in nums]
        # cmp(x,y), x>y : pos,
        tmp.sort(cmp = lambda x, y: cmp(x+y, y+x), reverse=True)

        res = ''.join(tmp)
        if res[0] == '0':
            return 0
        else:
            return res
        # print res

s = Solution()
s.largestNumber([3, 30, 34, 5, 9])

