# Count the number of prime numbers less than a non-negative number, n


class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes0(self, n):
        """
        1 classic prime check
        2 advanced approach: Sieve of Eratosthenes
        """
        count = 0
        for i in xrange(2, n+1):
            if self.isPrime(i):
                count += 1
        return count


    def isPrime(self, n):
        import math
        i = 2
        while i <= math.sqrt(n):
            if n % i == 0:
                return False
            i += 1
        return True


    def countPrimes(self, n):
        import sys
        """
        question:
            i * i <= n??  <=??
            j < n ??
         count: ~= n/ln(n)
         time: n log log n
        """
        if n < 2:
            return 0
        bitmap = [True] * n
        # print sys.getsizeof(bitmap)/1000/1000
        bitmap[0] = bitmap[1] = False
        i = 2
        while i * i < n:
            # print i
            if bitmap[i]:
                j = i + i
                while j < n:
                    bitmap[j] = False
                    j += i
            i += 1
        return sum(bitmap)



s = Solution()
print s.countPrimes(1000 * 1000 * 1)
# print s.isPrime(25)