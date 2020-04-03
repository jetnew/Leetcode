class Solution:
    def isHappy(self, n: int) -> bool:
        hist = []
        # Ref: https://www.johndcook.com/blog/2018/03/24/squared-digit-sum/
        attractors = [4, 16, 37, 58, 89, 145, 42, 20]
        ssr = 0
        while ssr != 1:
            if ssr in hist or ssr in attractors:
                return False
            hist.append(ssr)
            ssr = 0
            while n:
                ssr += (n % 10) ** 2
                n //= 10
            n = ssr
        return True

