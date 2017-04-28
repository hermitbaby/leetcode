# your code goes here


class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        result_list = []
        if numRows == 0:
            print result_list
            return result_list
        result_list.insert(0, [1])
        result_list.insert(1, [1, 1])


        deep = numRows
        for i in xrange(2, deep + 1):
            result_list.insert(i, [])
            result_list[i].append(1)
            # print result_list
            length = i
            for j in xrange(length - 1):
                result_list[i].append(result_list[i-1][j] + result_list[i-1][j+1])
            result_list[i].append(1)
        result = result_list[numRows]
        print result_list[:-1]
        return result_list[:-1]


a = Solution()
a.generate(2)
