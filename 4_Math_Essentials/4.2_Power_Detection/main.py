class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

if __name__ == '__main__':
    sol = Solution()
    
    print(f"Input: 1")
    print(f"Output: {sol.isPowerOfTwo(1)}")
    
    print(f"\nInput: 16")
    print(f"Output: {sol.isPowerOfTwo(16)}")
    
    print(f"\nInput: 3")
    print(f"Output: {sol.isPowerOfTwo(3)}")

    print(f"\nInput: 0")
    print(f"Output: {sol.isPowerOfTwo(0)}")

    print(f"\nInput: -16")
    print(f"Output: {sol.isPowerOfTwo(-16)}")