class Solution:
    def reverse(self, x: int) -> int:
        neg = 0
        if x < 0:
            neg = 1
            x *= -1

        val = 0

        while x:
            if val >= (2 ** 31 - 1) / 10:
                return 0

            val *= 10
            d = x % 10
            x = x // 10
            val += d

        if neg:
            val *= -1

        return val 