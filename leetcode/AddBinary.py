# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".


class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        lenA, lenB = len(a), len(b)
        lenLonger = lenA if lenA >= lenB else lenB
        lenShorter = lenA if lenA <= lenB else lenB

        if lenA == 0:
            return b
        if lenB == 0:
            return a

        aa = a[::-1]
        bb = b[::-1]
        strLonger = aa if len(a) >= len(b) else bb

        carry = 0
        result = []
        for i in xrange(lenLonger):
            if i < lenShorter:
                digit_sum = int(aa[i]) + int(bb[i]) + carry
                digit = digit_sum % 2
                result.append(str(digit))
                carry = digit_sum / 2
                if i == lenLonger - 1 and carry != 0 and lenA == lenB:
                    result.append(str(carry))
            else:
                digit_sum = int(strLonger[i]) + carry
                digit = digit_sum % 2
                result.append(str(digit))
                carry = digit_sum / 2
                if i == lenLonger - 1 and carry != 0:
                    result.append(str(carry))
        ret_string = ''.join(result)
        return ret_string[::-1]


s = Solution()
print s.addBinary('1', '1')
