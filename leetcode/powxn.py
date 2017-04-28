# implement power(x,n)



class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow0(self, x, n):
        """
        x^n = x^(n/2) * x^(n/2) * x^(n%2)
        if n is odd, then n/2 will lose precision, so need n%2 part
        """


        if n == 0 and x != 0:
            return 1
        if x == 0:
            return 0

        sum = 1
        for i in xrange(n):
            sum *= x

        return sum


    def myPow(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2: # odd n
            return self.myPow(x * x, n/2) * x
        else:
            return self.myPow(x * x, n/2)


s= Solution()
print s.myPow(2,10)