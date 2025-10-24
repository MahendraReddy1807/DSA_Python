class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    sol = Solution()
    
    input_str = "madam"
    print(f"Input: '{input_str}'")
    print(f"Output: {sol.isPalindrome(input_str)}")
    
    input_str_2 = "hello"
    print(f"\nInput: '{input_str_2}'")
    print(f"Output: {sol.isPalindrome(input_Sstr_2)}")
    
    input_str_3 = "racecar"
    print(f"\nInput: '{input_str_3}'")
    print(f"Output: {sol.isPalindrome(input_str_3)}")
    
    input_str_4 = "a"
    print(f"\nInput: '{input_str_4}'")
    print(f"Output: {sol.isPalindrome(input_str_4)}")