# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        """
        DP
            1 O(n * n) space
                for each node, calc the min sum
                from top to bottom, or from bottom to top
                if cannot modify the input, just deepcopy the input to a new working matrix
            2 O(n) space
            3 O(1) space
                directly use input matrix to store temp data
        """
        secLastRow = len(triangle)-2
        for i in xrange(secLastRow, -1, -1):
            for j in range(0, i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]
