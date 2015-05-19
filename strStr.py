# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        """
        string matching?
            brutal force
            KMP
        """

        if needle == '':
            return 0
        if needle != '' and haystack == '':
            return -1

        begin = 0
        while begin + len(needle) <= len(haystack):
            find = True
            for i in xrange(len(needle)):
                if haystack[begin + i] != needle[i]:
                    find = False
                    break
            if find:
                return begin
            begin += 1
        return -1


# special cases
# ('', '')
# ('abc', '')
s = Solution()
print s.strStr('mississippi', 'issip')
