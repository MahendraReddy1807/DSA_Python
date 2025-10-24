class Solution:
    def insertionSort(self, arr: list[int]) -> None:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        self.insertionSort(seats)
        self.insertionSort(students)
        
        total_moves = 0
        for i in range(len(seats)):
            total_moves += abs(seats[i] - students[i])
            
        return total_moves

if __name__ == '__main__':
    sol = Solution()
    
    seats1 = [3, 1, 5]
    students1 = [2, 7, 4]
    print(f"Input: seats = {seats1}, students = {students1}")
    print(f"Output: {sol.minMovesToSeat(seats1, students1)}")

    seats2 = [4, 1, 5, 9]
    students2 = [1, 3, 2, 6]
    print(f"\nInput: seats = {seats2}, students = {students2}")
    print(f"Output: {sol.minMovesToSeat(seats2, students2)}")