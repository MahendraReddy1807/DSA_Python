class Solution:
    def fibonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
            
        return b

if __name__ == '__main__':
    sol = Solution()
    
    input_num = 6
    print(f"Input: {input_num}")
    print(f"Output: {sol.fibonacci(input_num)}")
    
    input_num_2 = 0
    print(f"\nInput: {input_num_2}")
    print(f"Output: {sol.fibonacci(input_num_2)}")
    
    input_num_3 = 1
    print(f"\nInput: {input_num_3}")
    print(f"Output: {sol.fibonacci(input_num_3)}")
    
    input_num_4 = 2
    print(f"\nInput: {input_num_4}")
    print(f"Output: {sol.fibonacci(input_num_4)}")