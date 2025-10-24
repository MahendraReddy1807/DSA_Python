class Solution:
    def countEven(self, arr: list[int]) -> int:
        count = 0
        for num in arr:
            if num % 2 == 0:
                count += 1
        return count

if __name__ == '__main__':
    sol = Solution()
    
    input_arr = [2, 5, 6, 7, 8]
    print(f"Input: {input_arr}")
    print(f"Output: {sol.countEven(input_arr)}")
    
    input_arr_2 = [1, 3, 5, 7]
    print(f"\nInput: {input_arr_2}")
    print(f"Output: {sol.countEven(input_arr_2)}")
    
    input_arr_3 = [0, -2, -4]
    print(f"\nInput: {input_arr_3}")
    print(f"Output: {sol.countEven(input_arr_3)}")