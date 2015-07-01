class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}

    def dfs(self, n, k, string, stringlist):
        print stringlist
        if len(stringlist) == n:
            Solution.count += 1
            if Solution.count == k:
                # print stringlist
                Solution.res = stringlist
                return
                # return stringlist
        for i in range(len(string)):
            self.dfs(n, k, string[:i]+string[i+1:], stringlist+string[i])


    def getPermutation(self, n, k):
        string = ''
        for i in range(n):
            string += str(i+1)
        Solution.count = 0
        Solution.res = ''
        self.dfs(n, k, string, '')
        return Solution.res


s= Solution()
print s.getPermutation(9, 24)
