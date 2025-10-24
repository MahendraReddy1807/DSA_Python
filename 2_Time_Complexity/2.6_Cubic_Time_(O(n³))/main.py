class Solution:
    def printAllTriplets(self, arr: list[int]) -> None:
        for i in arr:
            for j in arr:
                for k in arr:
                    print(f"({i},{j},{k})")

if __name__ == '__main__':
    sol = Solution()
    
    print("Input: [1,2,3]")
    sol.printAllTriplets([1, 2, 3])
    
    print("\nInput: [4,5]")
    sol.printAllTriplets([4, 5])
    
    print("\nInput: [9]")
    sol.printAllTriplets([9])