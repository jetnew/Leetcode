class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""

        pf = strs[0]
        n = len(pf)
        for s in strs:
            i = 0
            m = len(s)
            while i < m and i < n:
                if pf[i] != s[i]:
                    n = i
                    break
                i += 1
            n = i

        return pf[:n]
