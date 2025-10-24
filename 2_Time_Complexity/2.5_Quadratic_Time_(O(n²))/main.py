class Solution:
    def printAllPairs(self, arr: list[int]) -> None:
        for i in arr:
            for j in arr:
                print(f"({i},{j})")

if __name__ == '__main__':
    sol = Solution()
    
    print("Input: [1,2,3]")
    sol.printAllPairs([1, 2, 3])
    
    print("\nInput: [5,6]")
    sol.printAllPairs([5, 6])
    
    print("\nInput: [7]")
    sol.printAllPairs([7])