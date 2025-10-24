class Solution:
    def sumArray(self, arr: list[int]) -> int:
        total_sum = 0
        for num in arr:
            total_sum += num
        return total_sum

if __name__ == '__main__':
    sol = Solution()
    print(sol.sumArray([2,4,6,8]))
    print(sol.sumArray([1]))
    print(sol.sumArray([-5,10,-3]))
    print(sol.sumArray([0,0,0,0]))