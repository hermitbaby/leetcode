# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.


class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        import string

        if s == '':
            return True
        start = 0
        end = len(s) - 1

        alphanumeric = string.ascii_lowercase + string.digits
        while start < end :
            # print start, end
            # how to implement lower() or upper() by hand
            # list(map(chr, range(ord('a'), ord('z')+1)))
            # chr(97) returns the string 'a'. This is the inverse of ord('a')
            # list(map(chr, range(ord('0'), ord('9')+1)))
            if s[start].lower() not in alphanumeric:
                start += 1
                continue
            if s[end].lower() not in alphanumeric:
                end -= 1
                continue
            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False
        return True


s = Solution()
ss = "A man, a plan, a canal: Panama"
ss2 = "race a car"
ss3 = ''
ss4 = 'aa'
ss5 = '1a2'
print s.isPalindrome(ss5)