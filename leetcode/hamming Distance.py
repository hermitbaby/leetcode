# -*- coding: utf-8 -*-

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        # b = max(x, y)
        # a = min(x, y)
        #
        # for i in xrange(32):
        #     if a << i == b:
        #         return i

        z = x^y
        # bin(z).count('1')

        count = 0
        while z!=0:
            if z & 1 == 1:      # 和1与，判断末尾是否为一
                count += 1
            z >>= 1

            # count += 1
            # z &= z - 1      # 和减一位与操作，操作count次数，能把z置成0

        # when s is str:
        # return sum(e1!=e2 for e1, e2 in zip(s1, s2))


        return count

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 10^9 < 2^32， 2^32 ~= 4 billion
        ans = 0
        for d in xrange(32):
            mask = 1 << d
            one, zero = 0, 0

            for num in nums:
                if num & mask:
                    one += 1
                else:
                    zero += 1
            ans += one * zero

        return ans


s = Solution()
print s.hammingDistance(1, 3)
print s.totalHammingDistance([4, 14, 2])