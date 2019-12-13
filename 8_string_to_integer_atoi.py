class Solution:
    def myAtoi(self, s: str) -> int:
        ls = [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9'
        ]
        p1 = 0
        n = len(s)
        sign = 1

        if n == 0:
            return 0

        # Remove whitespace
        while p1 < n and s[p1] == ' ':
            p1 += 1

        if p1 == n:
            return 0

        # Account for sign
        if s[p1] == '+' or s[p1] == '-':
            if s[p1] == '-':
                sign = -1
            p1 += 1

        # Return 0 if 1st non-whitespace is non-numerical/non-sign
        elif s[p1] not in ls:
            return 0

        # Find end of integer
        p2 = p1
        while p2 < n and s[p2] in ls:
            p2 += 1

        if s[p1:p2] != "":
            val = int(s[p1:p2])
        else:
            return 0
        val *= sign

        if val < -2 ** 31:
            return -2 ** 31
        if val > 2 ** 31 - 1:
            return 2 ** 31 - 1

        return val