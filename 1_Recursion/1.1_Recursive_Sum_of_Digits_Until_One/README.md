# Recursive Sum of Digits Until One
**Topic:** Recursion

**Type:** In-Session


Problem Statement: 

 You are given an integer n. 

 Your task is to determine, using recursion, the single-digit result obtained by repeatedly summing the digits of n until only one digit remains. 

Example 1: 
Input: n = 9875 
 Output: 2 

Explanation: 
 9 + 8 + 7 + 5 = 29 
 2 + 9 = 11 
 1 + 1 = 2 

Example 2: 
Input: n = 1234 
 Output: 1 

Explanation: 
 1 + 2 + 3 + 4 = 10 
 1 + 0 = 1 


Example 3: 
Input: n = 5 
 Output: 5 
Explanation: Already a single digit. 

 

Constraints: 
0 ≤ n ≤ 10⁹ 

### Approach
Describe your approach here...

### Pseudocode
```
FUNCTION solve(n):
    // Base case
    IF n < 10:
        RETURN n
    
    // Recursive step
    current_sum = 0
    WHILE n > 0:
        current_sum = current_sum + (n % 10)
        n = n // 10
    
    RETURN solve(current_sum)
```

### Time Complexity
- 
O(\log n)
### Space Complexity
- 
O(1)