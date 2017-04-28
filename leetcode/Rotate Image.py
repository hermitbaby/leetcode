# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Follow up:
# Could you do this in-place?



class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        # how to create a new n * n matrix in python?
        # how to copy all matrix value to new matrix
        # key point is index mapping
        # res_mtx[:][:] = matrix[:][:]

        n = len(matrix)

        # transpose a matrix
        for i in xrange(n):
            # pay attention to: j starts from i + 1
            for j in xrange(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in xrange(n):
            matrix[row].reverse()

        return matrix


s = Solution()
mtx = [[1,2,3], [4,5,6], [7,8,9]]
print s.rotate(mtx)