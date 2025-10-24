class Solution:
    def divideUntilOne(self, n: int) -> int:
        count = 0
        while n > 1:
            n //= 2
            count += 1
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.divideUntilOne(16))
    print(sol.divideUntilOne(8))
    print(sol.divideUntilOne(1))
    print(sol.divideUntilOne(100))