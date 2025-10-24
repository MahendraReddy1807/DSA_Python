class Solution:
    def removeDuplicates(self, arr: list[int]) -> int:
        if not arr:
            return 0
        
        k = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                arr[k] = arr[i]
                k += 1
        return k

if __name__ == '__main__':
    sol = Solution()
    
    input_arr = [1, 1, 2, 2, 3]
    print(f"Input: {input_arr}")
    new_length = sol.removeDuplicates(input_arr)
    print(f"Output: {new_length}")
    
    input_arr_2 = [1, 2, 3, 4, 5]
    print(f"\nInput: {input_arr_2}")
    new_length_2 = sol.removeDuplicates(input_arr_2)
    print(f"Output: {new_length_2}")

    input_arr_3 = [1, 1, 1, 1]
    print(f"\nInput: {input_arr_3}")
    new_length_3 = sol.removeDuplicates(input_arr_3)
    print(f"Output: {new_length_3}")