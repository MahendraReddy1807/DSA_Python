class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            
            if remainder == 0:
                return length
                
        return -1

if __name__ == '__main__':
    sol = Solution()
    
    k1 = 1
    print(f"Input: k = {k1}")
    print(f"Output: {sol.smallestRepunitDivByK(k1)}")
    
    k2 = 2
    print(f"\nInput: k = {k2}")
    print(f"Output: {sol.smallestRepunitDivByK(k2)}")
    
    k3 = 3
    print(f"\nInput: k = {k3}")
    print(f"Output: {sol.smallestRepunitDivByK(k3)}")
    
    k4 = 7
    print(f"\nInput: k = {k4}")
    print(f"Output: {sol.smallestRepunitDivByK(k4)}")