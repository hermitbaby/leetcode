# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.



class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        i = 0
        j = len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False


    def searchMatrix2(self, matrix, target):
        if len(matrix) == 0:
            return False

        # row, column
        m, n = len(matrix), len(matrix[0])
        # start, end
        s, e = 0, m * n - 1

        while s <= e:
            mid = (s + e) >> 1
            x, y = mid / n, mid % n

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                s += 1  # s = mid + 1
            else:
                e -= 1  # e = mid -1

        return False

