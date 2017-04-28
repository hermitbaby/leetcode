# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
#            eulb si yks eht
#            blue is sky the
# return "blue is sky the".
#
# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.
#
# click to show clarification.
#
# Clarification:
# What constitutes a word?
# A sequence of non-space characters constitutes a word.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing spaces.
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])


    def reverseWords2(self, s):
        """
        without extra space
            reverse whole string first, then reverse each word
        """
        rev1 = list(s[::-1])

        begin = 0
        for i in xrange(len(s) + 1):
            if i == len(s) or rev1[i] == ' ':
                self.reverse_pos(rev1, begin, i-1)
                begin = i + 1

        print rev1


    def reverse_pos(self, str, s, e):
        # str = list(str)
        i, j = s, e
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
        print str


s = Solution()
s.reverseWords2('hello my cat')

