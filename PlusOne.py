# Given a non-negative number represented as an array of digits, plus one to the number.
#
# The digits are stored such that the most significant digit is at the head of the list.


class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        """
        add from right most, if has carry, then add to left digit

        """
        if digits == None or digits == []:
            return digits

        rds = digits[::-1]
        # print rds
        carry = 1
        for i in xrange(len(digits)):
            digit = (rds[i] + carry) % 10
            carry = (rds[i] + carry) / 10
            rds[i] = digit
            if carry == 0:
                return rds[::-1]
        rds.append(1)
        # print result
        return rds[::-1]


s = Solution()
input = [1, 2, 3, 9, 9, 9]
input2 = [9, 9, 9, 9, 9, 0, 9]
print s.plusOne(input2)
