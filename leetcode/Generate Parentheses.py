#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"


class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 0:
            return []

        def dfs(l, r, item, res):
            if r < l:
                return
            if l == 0 and r == 0:
                res.append(item)
            if l > 0:
                print l-1, r, item + '(\t\t', res
                dfs(l - 1, r, item + '(', res)
            if r > 0:
                print l, r-1, item + ')\t\t', res
                dfs(l, r - 1, item + ')', res)


        res = []
        dfs(n, n, '', res)
        return res

s = Solution()

print s.generateParenthesis( 3 )