# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.


class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        """
        1 brutal force: O(n^3)
            O(n^2) to iterate all substring, O(n) to check if is palindromic
        2 DP
        3 iterate pivot
            O(n^2)
            optimaze version
        4 Manacher's Algorithm

        """
        p = ''
        for i in xrange(len(s)):
            # at least length for this iteration
            l = len(p) / 2
            # odd
            len1 = len(self.palin(s, i-l, i+l))
            if len1 > len(p):
                p = self.palin(s, i-l, i+l)
            # even
            len2 = len(self.palin(s, i-l, i + 1 + l))
            if len2 > len(p):
                p = self.palin(s, i-l, i + 1 + l)
        return p


    def palin(self, s, l, r):
        if l < 0 or r >= len(s):
            return ''
        else:
            str1 = s[l: r+1]
            str2 = str1[::-1]
            # if inner chars is palindromic, then check the outer chars
            if str1 == str2:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                return s[l+1: r]
            else:
                return ''



    # def longestPalindrome(self, s):
    #     """
    #     1 brutal force: O(n^3)
    #         O(n^2) to iterate all substring, O(n) to check if is palindromic
    #     2 DP
    #     3 iterate pivot
    #         O(n^2)
    #     4 Manacher's Algorithm
    #
    #     """
    #     p = ''
    #     for i in xrange(len(s)):
    #         # odd
    #         len1 = len(self.palin(s, i, i))
    #         if len1 > len(p):
    #             p = self.palin(s, i, i)
    #         # even
    #         len2 = len(self.palin(s, i, i + 1))
    #         if len2 > len(p):
    #             p = self.palin(s, i, i + 1)
    #     return p
    #
    #
    # def palin(self, s, l, r):
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         l -= 1
    #         r += 1
    #     return s[l+1: r]

