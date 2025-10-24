class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            
            j = i - 1
            
            is_key_even = (key % 2 == 0)
            
            while j >= 0:
                is_j_odd = (nums[j] % 2 != 0)
                
                if is_j_odd and is_key_even:
                    nums[j + 1] = nums[j]
                    j -= 1
                else:
                    break
                    
            nums[j + 1] = key
            
        return nums

if __name__ == '__main__':
    sol = Solution()
    
    nums1 = [3, 1, 2, 4]
    print(f"Input: {nums1}")
    print(f"Output: {sol.sortArrayByParity(nums1)}")
    
    nums2 = [0, 1, 2]
    print(f"\nInput: {nums2}")
    print(f"Output: {sol.sortArrayByParity(nums2)}")

    nums3 = [1, 3, 5, 2, 4, 6]
    print(f"\nInput: {nums3}")
    print(f"Output: {sol.sortArrayByParity(nums3)}")