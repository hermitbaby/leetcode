    # A -> 1
    # B -> 2
    # C -> 3
    # ...
    # Z -> 26
    # AA -> 27
    # AB -> 28
import string
import math

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        """
        Base 26 sum
        """
        dict = {}
        all = string.ascii_uppercase
        idx = 1
        for char in all:
            dict[char] = idx
            idx += 1
        # print dict

        sum = 0
        s2 = s[::-1]
        for x in xrange(0, len(s)):
            sum += dict[s2[x]] * math.pow(26, x)

        return int(sum)


    def convertToTitle(self, n):
        """
        While it's easy to convert any base number to base 10, but how to convert from base 10 to other base?
        how to deal with 0?
        """
        dict = {}
        all = string.ascii_uppercase
        idx = 1
        for char in all:
            # if idx == 26:
            #     break
            dict[idx] = char
            idx += 1
        # dict[0] = 'Z'
        # print dict

        result = []
        while n != 0:
            digit = n % 26
            if digit != 0:
                letter = dict[digit]
            else:
                letter = 'Z'
                n -= 1
            result.append(letter)
            n /= 26
        s = ''.join(result[::-1])
        return s
        # print s





s = Solution()
print s.titleToNumber('BBBBBB')

print s.convertToTitle(27)
