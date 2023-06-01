class Solution:
    def countPrimes(self, n: int) -> int:
        prime_nums = 0

        def isPrime(i):
            for m in range(2,i-1):
                if i%m == 0:
                    return False
            return True

        for p in range (2,n-1):
            if isPrime(p):
                prime_nums += 1
                
        return prime_nums
