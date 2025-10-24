class Solution:
    def findMax(self, arr: list[int]) -> int:
        if not arr:
            return None
        
        max_val = arr[0]
        for num in arr[1:]:
            if num > max_val:
                max_val = num
        return max_val

if __name__ == '__main__':
    sol = Solution()
    
    input_arr = [3, 7, 2, 9, 5]
    print(f"Input: {input_arr}")
    print(f"Output: {sol.findMax(input_arr)}")
    
    input_arr_2 = [-10, -5, -20, -1]
    print(f"\nInput: {input_arr_2}")
    print(f"Output: {sol.findMax(input_arr_2)}")
    
    input_arr_3 = [42]
    print(f"\nInput: {input_arr_3}")
    print(f"Output: {sol.findMax(input_arr_3)}")