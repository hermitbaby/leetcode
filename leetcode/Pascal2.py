# your code goes here


class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        result = []
        result_list = []
        result_list.insert(0, [1])
        result_list.insert(1, [1, 1])
        if rowIndex == 0:
            result = result_list[0]
        elif rowIndex == 1:
            result = result_list[1]
        elif rowIndex > 1:
            deep = rowIndex
            for i in xrange(2, deep + 1):
                result_list.insert(i, [])
                result_list[i].append(1)
                # print result_list
                length = i
                for j in xrange(length - 1):
                    result_list[i].append(result_list[i-1][j] + result_list[i-1][j+1])
                result_list[i].append(1)
            result = result_list[rowIndex]
        print result_list
        return result_list


a = Solution()
a.getRow(5)
