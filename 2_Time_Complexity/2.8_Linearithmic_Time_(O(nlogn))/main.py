class Solution:
    def printLinearithmic(self, n: int) -> None:
        while n > 0:
            for i in range(1, n + 1):
                print(i, end=" ")
            print()
            n //= 2

if __name__ == '__main__':
    sol = Solution()
    
    print("Input: n=8")
    sol.printLinearithmic(8)
    
    print("\nInput: n=5")
    sol.printLinearithmic(5)
    
    print("\nInput: n=1")
    sol.printLinearithmic(1)