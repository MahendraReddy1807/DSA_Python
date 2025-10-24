class Solution:
    def sumArray(self, arr: list[int]) -> int:
        total_sum = 0
        for num in arr:
            total_sum += num
        return total_sum

if __name__ == '__main__':
    sol = Solution()
    
    input_arr = [1, 2, 3]
    print(f"Input: {input_arr}")
    print(f"Output: {sol.sumArray(input_arr)}")
    
    input_arr_2 = [10, -5, 2]
    print(f"\nInput: {input_arr_2}")
    print(f"Output: {sol.sumArray(input_arr_2)}")