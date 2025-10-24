class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 4 == 0:
            n //= 4
            
        return n == 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfFour(16))
    print(sol.isPowerOfFour(5))
    print(sol.isPowerOfFour(1))
    print(sol.isPowerOfFour(-1))