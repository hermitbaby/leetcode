# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
#


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        """
        1 intuitive idea
            get all length of substring, from n, n-1, n-2, ... , 2, 1
            see if they have duplicated element: len(list()) == len(set())
        2 dp
            if has duplicate element, left pointer jumps to pre duplicate element index + 1
            see the explanation pic in xiaoyu blog
        """

        res = 0
        left = 0
        d = {}

        # enumerate() can access both index and content
        for i, ch in enumerate(s):
            if ch in d and d[ch] >= left:
                left = d[ch] + 1
                # print left
            d[ch] = i
            res = max(res, i - left + 1)
        # print d
        return res


s = Solution()
str = 'qpxrjxkltzyx'
print s.lengthOfLongestSubstring('qpxrjxkltzyx')