class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def recur(lst, val):
            if val == 0:
                ans.append(lst.copy())
            if val < 0:
                return
            for c in candidates:
                if lst == []:
                    nlst = lst.copy()
                    nlst.append(c)
                    recur(nlst, val - c)
                elif c >= lst[-1]:
                    nlst = lst.copy()
                    nlst.append(c)
                    recur(nlst, val - c)
        recur([], target)
        return ans