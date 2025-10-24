class Solution:
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
            
        result = 1
        for i in range(1, n + 1):
            result *= i
            
        return result

if __name__ == '__main__':
    sol = Solution()
    
    input_num = 5
    print(f"Input: {input_num}")
    print(f"Output: {sol.factorial(input_num)}")
    
    input_num_2 = 0
    print(f"\nInput: {input_num_2}")
    print(f"Output: {sol.factorial(input_num_2)}")
    
    input_num_3 = 1
    print(f"\nInput: {input_num_3}")
    print(f"Output: {sol.factorial(input_num_3)}")