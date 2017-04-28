# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.


class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, strs):
        """
        special cases:
            1 empty str
            2 invalid str, like alphabet letter, not number
                whitespace?
                characters after valid string
                sign of +/-
            3 overflow

        Idea:
            dict to store string to int mapping
                '1' --> 1
                '2' --> 2
            use ord() to find ascii number of a letter
                python does not support str -str, while c/c++ does
        """
        INT_MAX, INT_MIN = 2147483647, -2147483648

        index = 0
        pos = True
        result = 0

        if len(strs) == 0:
            return 0
        while strs[index] == ' ':
            index += 1

        if strs[index] == '-':
            pos = False
        if strs[index] in '-+':
            index += 1

        nums = set()
        for j in xrange(10):
            nums.add(str(j))

        while index < len(strs) and strs[index] in nums:
            result = 10 * result + ord(strs[index]) - ord('0')
            index += 1

            if pos and result >= INT_MAX:
                return INT_MAX
            if not pos and -result <= INT_MIN:
                return INT_MIN

        return result if pos else -result


s = Solution()
print s.myAtoi('-2147483649')
