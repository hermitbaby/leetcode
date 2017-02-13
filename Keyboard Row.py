# -*- coding: utf-8 -*-

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows= [
            set('qwertyuiop'),
            set('asdfghjkl'),
            set('zxcvbnm')
        ]

        res = []
        for word in words:
            w = set(word.lower())

            for r in rows:
                if w <= r:
                    res.append(word)

        return res

s= Solution()
print s.findWords(["Hello", "Alaska", "Dad", "Peace"])


