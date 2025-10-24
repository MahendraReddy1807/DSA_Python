class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        result_sum = num1 + num2
        return bin(result_sum)[2:]

if __name__ == '__main__':
    sol = Solution()
    
    a1, b1 = "11", "1"
    print(f"Input: a = \"{a1}\", b = \"{b1}\"")
    print(f"Output: \"{sol.addBinary(a1, b1)}\"")
    
    a2, b2 = "1010", "1011"
    print(f"\nInput: a = \"{a2}\", b = \"{b2}\"")
    print(f"Output: \"{sol.addBinary(a2, b2)}\"")