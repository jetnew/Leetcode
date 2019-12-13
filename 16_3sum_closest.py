class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def diff(val, target):
            return abs(val - target)
        def midpt(p1, p2):
            return (p1+p2)//2
        def ssum(p1, p2, p3):
            return nums[p1] + nums[p2] + nums[p3]
        def fin(p1, p2, p3):
            return p2-p1 == 1 and p3-p2 == 1 or p2 >= p3

        nums = sorted(nums)
        # print(nums)
        n = len(nums)
        p1 = 0
        p2 = p1 + 1
        p3 = n-1
        # print(nums[:3])
        closest = sum(nums[:3])
        cdiff = diff(closest, target)

        # print("closest:", closest)

        # Main loop
        for p1 in range(n-2):  # while not all diff by 1
            p2 = p1 + 1
            p3 = n-1
            # print("while1")
            # print(p1, p2, p3)
            val = nums[p1] + nums[p2] + nums[p3]
            # print(val)

            # Search the window
            while p2 < p3:
                # print("while3")
                val = ssum(p1, p2, p3)
                # print("val:", val)
                d = val - target
                dd = diff(val, target)
                # print("dd:", dd)
                if dd < cdiff:
                    # print("dd:",dd)
                    cdiff = dd
                    closest = val
                if d > 0:  # if bigger, close window from right
                    p3 -= 1
                elif d < 0:  # if smaller, close window from left
                    p2 += 1
                else:
                    return val

        return closest
