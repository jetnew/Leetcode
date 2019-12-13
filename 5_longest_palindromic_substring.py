class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Odd length
        # For each char, have 2 pointers on the char index

        # Even length
        # For each char, have 1 pointer on char index, the other at char+1 index

        # While chars are equal, increment and decrement the 2 pointers respectively
        # If longer than longest substring, update longest substring
        # Update by slicing string from start to end pointer index

        longest = ""

        if len(s) <= 1:
            longest = s

        if len(s) == 2:
            longest = s[0]

        for i, c in enumerate(s[:-1]):
            p1, p2 = i, i
            while s[p1] == s[p2]:
                if p1 == 0 or p2 == len(s) - 1:
                    break
                p1 -= 1
                p2 += 1

            if s[p1] != s[p2]:
                p1 += 1
                p2 -= 1

            if p2 - p1 + 1 > len(longest):
                longest = s[p1:p2 + 1]

            p1, p2 = i, i + 1
            while s[p1] == s[p2]:
                if p1 == 0 or p2 == len(s) - 1:
                    break
                p1 -= 1
                p2 += 1

            if s[p1] != s[p2]:
                p1 += 1
                p2 -= 1

            if p2 - p1 + 1 > len(longest):
                longest = s[p1:p2 + 1]

        return longest