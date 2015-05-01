# Example: 19 is a happy number
#
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy0(self, n):
        # digits = []
        # num = n
        # while num != 0:
        #     digit = num % 10
        #     digits.append()

        digits = str(n)
        sum = 0
        for d in digits:
            sum += int(d) * int(d)
        if sum == 1:
            return True
        else:
            return self.isHappy(sum)

    def isHappy(self, n):
        """
        1 use set to check if loop endless
        2 terminate condition for loop
        """
        num_set = set()
        while n not in num_set:
            num_set.add(n)

            digits = str(n)
            sum = 0
            for d in digits:
                sum += int(d) * int(d)
            print digits, sum
            n = sum

            if n == 1:
                return True
        return False



s = Solution()
print s.isHappy(20)