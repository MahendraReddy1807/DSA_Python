class Solution:
    def insertionSort(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
            
        return nums

if __name__ == '__main__':
    sol = Solution()
    
    nums1 = [5, 2, 3, 1]
    print(f"Input: {nums1}")
    print(f"Output: {sol.insertionSort(nums1)}")
    
    nums2 = [5, 1, 1, 2, 0, 0]
    print(f"\nInput: {nums2}")
    print(f"Output: {sol.insertionSort(nums2)}")