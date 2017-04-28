# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if matrix == []:
            return []

        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0

        # 0: go right, 1: go down, 2: go left, 3:go up
        direct = 0
        res = []

        while True:
            if direct == 0:
                for i in xrange(left, right+1):
                    res.append(matrix[top][i])
                top += 1

            if direct == 1:
                for i in xrange(top, bottom+1):
                    res.append(matrix[i][right])
                right -= 1

            if direct == 2:
                for i in xrange(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if direct == 3:
                for i in xrange(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1

            if left > right or top > bottom:
                return res

            direct = (direct + 1) % 4


    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n == 0:
            return []

        matrix = [ [0] * n for i in xrange(n)]
        # !!! matrix, n 1-d array is the same array!
        # matrix = [[0] * n ] * n 
        # matrix = [[0 for i in xrange(n)] for i in xrange(n)]

        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0

        # 0: go right, 1: go down, 2: go left, 3:go up
        direct = 0
        count = 0

        while True:
            if direct == 0:
                # # print matrix
                for i in xrange(left, right+1):
                    count += 1
                    matrix[top][i] = count
                # print matrix
                top += 1

            if direct == 1:
                for i in xrange(top, bottom+1):
                    count += 1
                    matrix[i][right] = count
                # print matrix
                right -= 1

            if direct == 2:
                for i in xrange(right, left-1, -1):
                    count += 1
                    matrix[bottom][i] = count
                # print matrix
                bottom -= 1

            if direct == 3:
                for i in xrange(bottom, top-1, -1):
                    count += 1
                    matrix[i][left] = count
                # print matrix
                left += 1

            if count == n * n :
                return matrix

            direct = (direct + 1) % 4



s = Solution()
# print s.spiralOrder([[1,2,3], [4,5,6], [7,8,9]])
print s.generateMatrix(4)

