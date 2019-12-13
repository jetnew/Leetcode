class Solution:
    def romanToInt(self, s: str) -> int:
        ref = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        val = 0
        n = len(s)
        i = 0
        while i < n:
            if i + 1 < n:
                if s[i] == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    val += ref[s[i + 1]] - ref[s[i]]
                    i += 2
                elif s[i] == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    val += ref[s[i + 1]] - ref[s[i]]
                    i += 2
                elif s[i] == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    val += ref[s[i + 1]] - ref[s[i]]
                    i += 2
                else:
                    val += ref[s[i]]
                    i += 1
            else:
                val += ref[s[i]]
                i += 1

        return val
