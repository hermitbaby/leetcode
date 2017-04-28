# Write a function to find the longest common prefix string amongst an array of strings.


class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        result = ['']
        for i in xrange(len(strs[0])):
            for j in xrange(1, len(strs)):
                # print j
                # must be <=, not just <
                if len(strs[j]) <= i or strs[0][i] != strs[j][i]:
                    return result[-1]
            result.append(strs[0][:i+1])
            # print result
        return result[-1]



s = Solution()
strs = ['', '']
strs2 = ['abcdef', 'abcde', 'abcdf', 'ab']
print s.longestCommonPrefix(strs)
