# Given two numbers represented as strings, return multiplication of the numbers as a string.
#
# Note: The numbers can be arbitrarily large and are non-negative.


class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        """
        mimic raw multiply for two numbers
            - removing ending zero, add them at last
            -
        """
        num1 = num1[::-1]
        num2 = num2[::-1]

        tmp_res = [0 for i in xrange(len(num1) + len(num2))]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                tmp_res[i + j] += int(num1[i]) * int(num2[j])

        result = []
        for i in xrange(len(tmp_res)):
            digit = tmp_res[i] % 10
            carry = tmp_res[i] / 10

            if i < len(tmp_res) -1:
                tmp_res[i+1] += carry
            result.insert(0, str(digit))

        while result[0] == '0' and len(result) > 1:
            del result[0]

        return ''.join(result)


    def multiply2(self, num1, num2):
        """
        mimic raw multiply for two numbers
            - removing ending zero, add them at last
            -
        """
        num1 = num1[::-1]
        num2 = num2[::-1]

        tmp_res = [0 for i in xrange(len(num1) + len(num2))]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                tmp_res[i + j] += int(num1[i]) * int(num2[j])

        # tmp_res = tmp_res[::-1]
        # print tmp_res
        result = []
        for i in xrange(len(tmp_res)):
            digit = tmp_res[i] % 10
            carry = tmp_res[i] / 10

            if i < len(tmp_res) -1:
                tmp_res[i+1] += carry
            result.insert(0, str(digit))

        while result[0] == '0' and len(result) > 1:
            del result[0]

        return ''.join(result)


s = Solution()
print s.multiply2('123', '456')

# reverse tmp_res
# [0, 18, 27, 28, 13, 4]
# 560880

# reverse num1 & num2
# [18, 27, 28, 13, 4, 0]
# 56088