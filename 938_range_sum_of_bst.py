# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def recur(node, L, R, sum):
            if node is None:
                return sum
            if L <= node.val <= R:
                sum += node.val
            if node.val < R:
                sum = recur(node.right, L, R, sum)
            if node.val > L:
                sum = recur(node.left, L, R, sum)
            return sum
        return recur(root, L, R, 0)
