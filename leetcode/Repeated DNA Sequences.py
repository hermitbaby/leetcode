# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].



class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        dict = {}
        result = []

        for i in xrange(len(s)):
            # end index
            endIdx = i + 10
            if endIdx <= len(s):
                substr = s[i:i+10]
                print substr
                dict[substr] = dict.get(substr, 0) + 1

        for k in dict:
            if dict[k] > 1:
                result.append(k)

        return result


s = Solution()
print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")