# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
# click to show follow up.
#
# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        rowNum = len(matrix)
        colNum = len(matrix[0])

        row0 = set()
        col0 = set()

        for i in xrange(rowNum):
            for j in xrange(colNum):
                if matrix[i][j] == 0:
                    row0.add(i)
                    col0.add(j)

        for i in row0:
            for j in xrange(colNum):
                matrix[i][j] = 0

        for j in col0:
            for i in xrange(rowNum):
                matrix[i][j] = 0
