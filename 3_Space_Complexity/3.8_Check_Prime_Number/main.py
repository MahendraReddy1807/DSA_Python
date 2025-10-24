class Solution:
    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
            
        return True

if __name__ == '__main__':
    sol = Solution()
    
    input_num = 7
    print(f"Input: {input_num}")
    print(f"Output: {sol.isPrime(input_num)}")
    
    input_num_2 = 10
    print(f"\nInput: {input_num_2}")
    print(f"Output: {sol.isPrime(input_num_2)}")
    
    input_num_3 = 2
    print(f"\nInput: {input_num_3}")
    print(f"Output: {sol.isPrime(input_num_3)}")
    
    input_num_4 = 9
    print(f"\nInput: {input_num_4}")
    print(f"Output: {sol.isPrime(input_num_4)}")