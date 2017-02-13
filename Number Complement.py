# -*- coding: utf-8 -*-

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        start = False

        for i in xrange(31, -1, -1):   # 找到最高位是1的，记录下；之后的num位数置反位
            if (num & (1<< i)):
                start = True
            if start:
                num ^= (1<<i)

        # 另： 找到需要置反位的，其余和0与，都置0
        # mask = INT_MAX;
        # while (mask & num) mask <<= 1;
        # return ~mask & ~num;

        return num

