from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        n = len(nums)
        
        def backtrack(current_perm, counter):
            if len(current_perm) == n:
                result.append(list(current_perm))
                return
            
            for num in counter:
                if counter[num] > 0:
                    current_perm.append(num)
                    counter[num] -= 1
                    
                    backtrack(current_perm, counter)
                    
                    current_perm.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))
        return result

if __name__ == '__main__':
    sol = Solution()
    
    nums1 = [1, 1, 2]
    print(f"Input: {nums1}")
    print(f"Output: {sol.permuteUnique(nums1)}")
    
    nums2 = [1, 2, 3]
    print(f"\nInput: {nums2}")
    print(f"Output: {sol.permuteUnique(nums2)}")