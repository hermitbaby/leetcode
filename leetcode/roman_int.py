# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.

# I II III IV V VI VII VIII IX X
# XL 40, L 50, LX 60
# XC 90, C 100
# D 500, M 1000, MD 1500
# 3999: MMMIM xx
#       MMMCMXCIX

# You must separate ones, tens, hundreds, and thousands as separate items.
# That means that 99 is XCIX, 90 + 9, but never should be written as IC.
# Similarly, 999 cannot be IM and 1999 cannot be MIM.



class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        # int to roman?!
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return dict[s[0]]
        sum += dict[s[0]]
        for i in xrange(1, len(s)):
            if dict[s[i]] <= dict[s[i-1]]:
                sum += dict[s[i]]
            elif dict[s[i]] > dict[s[i-1]]:
                sum += dict[s[i]] - 2 * dict[s[i-1]]

        return sum


s = Solution()
print s.romanToInt('MMMCMXCIX')