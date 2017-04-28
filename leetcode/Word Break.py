# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        """
        DP
            try to understand the check condition:
            if first k element(dp[k]) in dict, check whether the remaining word in dict

        """
        # print type(s)
        dp = [False for i in range(len(s)+1)]
        dp[0] = True

        for i in range(1, len(s)+1):
            for k in range(i):
                print i, 'dp[', k, ']', dp[k], s[k:i]
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True

        print dp
        return dp[len(s)]


sol= Solution()
s = "leetcode"
dict = ["leet", "code"]
print sol.wordBreak(s, dict)