class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(start_index, current_subset):
            result.append(list(current_subset))
            
            for i in range(start_index, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
                
        backtrack(0, [])
        return result

if __name__ == '__main__':
    sol = Solution()
    
    print(f"Input: [1,2] -> Output: {sol.subsets([1, 2])}")
    print(f"Input: [3] -> Output: {sol.subsets([3])}")
    
    subsets_123 = sol.subsets([1, 2, 3])
    print(f"Input: [1,2,3] -> Output: {len(subsets_123)} subsets")
    print(subsets_123)