class Solution:
    def maxArea(self, height: List[int]) -> int:
        biggest_vol = 0
        i = 0
        j = len(height) - 1

        while i != j:
            breadth = abs(i - j)
            vol = min(height[i], height[j]) * breadth
            if vol > biggest_vol:
                biggest_vol = vol

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return biggest_vol