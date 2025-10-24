class Solution:
    def maxOfTwo(self, a: int, b: int) -> int:
        if a >= b:
            return a
        else:
            return b

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxOfTwo(7, 12))
    print(sol.maxOfTwo(-5, -10))
    print(sol.maxOfTwo(100, 100))