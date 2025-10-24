class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        
        if len(arr) <= 2:
            return True
            
        diff = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
                
        return True

if __name__ == '__main__':
    sol = Solution()
    
    arr1 = [3, 5, 1]
    print(f"Input: {arr1}")
    print(f"Output: {sol.canMakeArithmeticProgression(arr1)}")
    
    arr2 = [1, 2, 4]
    print(f"\nInput: {arr2}")
    print(f"Output: {sol.canMakeArithmeticProgression(arr2)}")