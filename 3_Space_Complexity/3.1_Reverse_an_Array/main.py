class Solution:
    def reverseArray(self, arr: list[int]) -> list[int]:
        left = 0
        right = len(arr) - 1
        
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
        return arr

if __name__ == '__main__':
    sol = Solution()
    
    input_arr = [1, 2, 3, 4, 5]
    print(f"Input: {input_arr}")
    print(f"Output: {sol.reverseArray(input_arr)}")
    
    input_arr_2 = [10, 20, 30]
    print(f"\nInput: {input_arr_2}")
    print(f"Output: {sol.reverseArray(input_arr_2)}")