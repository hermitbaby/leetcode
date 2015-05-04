# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#        aad
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dict1 = {}
        dict2 = {}
        for i in xrange(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = t[i]
            if t[i] not in dict2:
                dict2[t[i]] = s[i]
            # checking
            if dict1[s[i]] != t[i] or \
                dict2[t[i]] != s[i]:
                return False
        return True
        # 1 check dict length
        # 2 check t order


s = Solution()
print s.isIsomorphic('egg', 'aad')
