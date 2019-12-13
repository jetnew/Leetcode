class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        m = 2 * (numRows - 1)

        zigzag = []
        for i in range(numRows):
            zigzag.append([])

        for i, c in enumerate(s):
            if i % m <= numRows - 1:
                zigzag[i % m].append(c)
            else:
                zigzag[(i // m + 1) * m - i].append(c)

        return "".join(["".join(zz) for zz in zigzag])
