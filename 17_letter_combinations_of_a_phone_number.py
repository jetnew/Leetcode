class Solution:
    dic = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    mem = {}

    def letterCombinations(self, digits: str) -> List[str]:
        if digits in Solution.mem:
            return Solution.mem[digits]
        if digits == "":
            return []
        if len(digits) == 1:
            return Solution.dic[digits]
        rest = self.letterCombinations(digits[1:])
        lst = []
        for c in Solution.dic[digits[0]]:
            lst += [c + r for r in rest]
        Solution.mem[digits] = lst
        return Solution.mem[digits]

