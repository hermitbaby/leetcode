# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]


class Solution:
    # @param s, a string
    # @return a list of lists of string
    def isPalindrome(self, s):
        # for i in range(len(s)):
        #     if s[i] != s[len(s)-1-i]: return False
        # return True
        b, e = 0, len(s)-1
        while b < e:
            if s[b] != s[e]:
                return False
            b += 1
            e -= 1
        return True


    # def dfs(self, s, stringlist):
    #     if len(s) == 0: Solution.res.append(stringlist)
    #     for i in range(1, len(s)+1):
    #         if self.isPalindrome(s[:i]):
    #             self.dfs(s[i:], stringlist+[s[:i]])
    #
    # def partition(self, s):
    #     Solution.res = []
    #     self.dfs(s, [])
    #     return Solution.res

    def partition(self, s):

        def dfs(s, strList):
            if len(s) == 0:
                res.append(strList)

            # lopping for each length, form 1 to 2, 3, 4, ..., len(s)
            for i in xrange(1, len(s) + 1):
                print s[:i]
                if self.isPalindrome(s[:i]):
                    print s[i:], strList + [s[:i]]
                    dfs(s[i:], strList + [s[:i]])

        res = []
        dfs(s, [])
        return res


s = Solution()
print s.partition('aab')
