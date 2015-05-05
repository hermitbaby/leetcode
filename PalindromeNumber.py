# Determine whether an integer is a palindrome. Do this without extra space.
#
# click to show spoilers.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.


class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        """
        1 reverse the int, then compare
        2 directly compare
        """
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10

        while x != 0:
            left = x / div
            right = x % 10

            if left != right :
                return False

            # 12321 --> 232
            x = (x % div) / 10
            div /= 10 * 10
        return True

s = Solution()
print s.isPalindrome(123211)