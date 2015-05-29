# Given an array of strings, return all groups of strings that are anagrams.
#
# Note: All inputs will be in lower-case.


class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        dict = {}

        for str in strs:
            key = ''.join(sorted(str))
            if key not in dict:
                dict[key] = [str]
            else:
                dict[key] += [str]

        result = []
        for key in dict:
            if len(dict[key]) > 1:
                result.extend(dict[key])
        return result
