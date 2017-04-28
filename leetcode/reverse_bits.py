# Reverse bits of a given 32 bits unsigned integer.
#
# For example, given input 43261596  , return 964176192
# (represented in binary as 00000010100101000001111010011100),
# (represented in binary as 00111001011110000010100101000000).

# reverse is not bit 'not' operation
# 000010100101000001111010011100
# 111001011110000010100101000000

import math

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        reverse = ''
        for i in xrange(32):
            if n & 1 == 1:
                reverse = reverse + '1'
            else:
                reverse = reverse + '0'
            n >>= 1
        # bin 2 int
        ret = 0
        for i in xrange(32):
            if reverse[31-i] == '1':
                ret += math.pow(2, i)
            else:
                continue
        return int(ret)



s = Solution()
print s.reverseBits(43261596)

