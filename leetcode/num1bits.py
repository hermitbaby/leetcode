# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.


class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        # int to binary
        bin = ''
        count = 0
        if n == 0:
            bin = '0'
        while n:
            # check last digit
            if n & 1 == 1:
                bin = '1' + bin
                count += 1
            else:
                bin = '0' + bin
            n >>= 1
        return count


s = Solution()
print s.hammingWeight(0)
