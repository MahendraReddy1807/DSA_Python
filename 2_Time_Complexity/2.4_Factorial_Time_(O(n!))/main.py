from itertools import permutations

class Solution:
    def allPermutations(self, s: str) -> list[str]:
        perms = permutations(s)
        result = [''.join(p) for p in perms]
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.allPermutations("abc"))
    print(sol.allPermutations("ab"))
    print(sol.allPermutations("a"))