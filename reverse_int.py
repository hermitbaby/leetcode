# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321


class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse0(self, x):
        my_str = ''
        neg = True if x < 0 else False
        num = -x if x < 0 else x
        if x == 0:
            return 0
        while num != 0 :
            last_digit = num % 10
            my_str = my_str + str(last_digit)
            num = num / 10
        ret_num = -int(my_str) if neg else int(my_str)
        return ret_num

    def reverse(self, x):
        my_str = ''
        neg = True if x < 0 else False
        num = -x if x < 0 else x
        result = 0
        if x == 0:
            return 0
        while num != 0 :
            last_digit = num % 10
            result = result * 10 + last_digit
            num = num / 10
        # ret_num = -int(my_str) if neg else int(my_str)
        # max int number in C, but python will not overflow
        ret_num = result if result < 2147483647 else 0
        ret_num = -ret_num if neg else ret_num
        return ret_num




s = Solution()
print s.reverse(1534236469)

