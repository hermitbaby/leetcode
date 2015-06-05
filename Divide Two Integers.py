# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.


class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        cur = dividend
        count = 0
        while cur - divisor >= 0:
            cur -= divisor
            count += 1
        return count


    def divide2(self, dividend, divisor):
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        sum = 0
        count = 0
        res = 0
        a = abs(dividend)
        b = abs(divisor)
        while a >= b:
            sum = b
            # print 'outer', sum
            count = 1
            while sum + sum <= a:
                sum += sum
                count += count
                # print 'inner', sum, count
            a -= sum
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        # handle int_max: 2^31 -1 , signed number
        if res > 2147483647:
            res = 2147483647
        return res


s = Solution()
print s.divide2(	-2147483648, -1)
