# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        """
        first impression is to use split(), then just length;
        but may have multiple spaces between word
            'hello wo  rld  '
        """
        if s == None or s == '':
            return 0

        idx = len(s) - 1
        while idx >= 0 and s[idx] == ' ':
            idx -= 1

        idx2 = idx
        while idx2 >= 0 and s[idx2] != ' ':
            idx2 -= 1

        return idx - idx2


s = Solution()
str= 'hello wo  rld  '
print s.lengthOfLastWord('   ')
