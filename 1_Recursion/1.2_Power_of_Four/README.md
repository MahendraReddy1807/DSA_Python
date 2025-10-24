# Power of Four
**Topic:** Recursion

**Type:** Home Challenge


Problem Statement: 

 Given an integer n, return true if it is a power of four. Otherwise, return false. 

An integer n is a power of four if there exists an integer x such that n == 4^x. 

 

Example 1: 

Input: n = 1 

 Output: true 

 Explanation: 4⁰ = 1 

 

Example 2: 

Input: n = 16 

 Output: true 

 Explanation: 4² = 16 

 

Example 3: 

Input: n = 8 

 Output: false 

 Explanation: Although 8 is a power of two, it is not a power of four. 

 

Example 4: 

Input: n = 0 

 Output: false 

 

Example 5: 

Input: n = -4 

 Output: false 

 

Constraints: 

−2³¹ ≤ n ≤ 2³¹ − 1 

### Approach
Describe your approach here...

### Pseudocode
```
Write your pseudocode here...
```
FUNCTION isPowerOfFour(n):
    IF n == 1:
        RETURN True
    
    IF n <= 0 OR n % 4 != 0:
        RETURN False
        
    RETURN isPowerOfFour(n // 4)
### Time Complexity
- 
O(log n)
### Space Complexity
- 
O(log n)