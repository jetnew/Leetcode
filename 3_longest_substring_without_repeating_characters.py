class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 1

        curr = s[p1:p2]

        longest = curr
        longest_n = len(longest)
        m = len(s)

        while p2 < m and p1 < m:
            if s[p2] in curr:
                p1 += 1
            else:
                p2 += 1

            curr = s[p1:p2]
            curr_n = p2 - p1
            if curr_n > longest_n:
                longest = curr
                longest_n = curr_n

        return longest_n

