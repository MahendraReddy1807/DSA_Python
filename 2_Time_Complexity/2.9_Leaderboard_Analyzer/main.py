class Solution:
    def analyzeScores(self, scores: list[int]) -> None:
        if not scores:
            print("No scores provided.")
            return

        n = len(scores)

        # 1. Find Highest Score
        highest_score = scores[0]
        total_sum = 0
        for score in scores:
            if score > highest_score:
                highest_score = score
            total_sum += score
        
        print(f"Highest Score: {highest_score}")

        # 2. Compute Average Score
        average_score = total_sum / n
        print(f"Average Score: {average_score}")

        # 3. Count Above Average
        above_average_count = 0
        for score in scores:
            if score > average_score:
                above_average_count += 1
        
        print(f"Students Above Average: {above_average_count}")

        # 4. Print Rank List (using built-in sort)
        scores.sort(reverse=True)
        print(f"Rank List: {scores}")

if __name__ == '__main__':
    sol = Solution()
    
    print("Input: [50, 70, 90, 60, 80]")
    sol.analyzeScores([50, 70, 90, 60, 80])
    
    print("\nInput: [30, 30, 30]")
    sol.analyzeScores([30, 30, 30])
    
    print("\nInput: [100, 40, 60, 80]")
    sol.analyzeScores([100, 40, 60, 80])