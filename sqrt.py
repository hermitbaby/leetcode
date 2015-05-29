# sqrt()


class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        """
        binary search
        """
        if x == 0:
            return 0

        i = 0
        j = x / 2 + 1
        while i <= j:
            center = (i + j) / 2
            print i,j, center
            if center ** 2 == x:
                return center
            elif center ** 2 < x:
                i = center + 1
            else:
                j = center -1
        # if x = 2
        return j



s = Solution()
print s.mySqrt(4)