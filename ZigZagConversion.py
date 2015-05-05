# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N    0 4 8    numRow+1
# A P L S I I G    1 3 5    numRow-1
# Y   I   R        2 6      numRow+1
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        """
        one zigzag group size: 2*numRows - 2
        if i >= numRows, line num should be: group - i
        """
        if numRows == 1:
            return s
        group = 2 * numRows - 2
        strline = []
        for j in xrange(numRows):
            strline.append([])
        # print strline
        for i in xrange(len(s)):
            new_i = i % group
            if i % group < numRows:
                strline[new_i].append(s[i])
            else:
                strline[group - new_i].append(s[i])
        # print strline
        # bb = [''.join(line) for line in strline]
        # print bb
        result = ''.join([''.join(line) for line in strline])
        return result


s = Solution()
print s.convert("PAYPALISHIRING", 5)

