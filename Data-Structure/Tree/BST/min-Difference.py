# https://leetcode.com/problems/minimum-absolute-difference-in-bst/


def getMinimumDifference(root):
    minDiff = lastVal = float("inf")
       # traverse inorderly to create a sorted arr

    def dfs(root):
        if not root:
            return

        dfs(root.left)
        minDiff = min(abs(root.val - lastVal), minDiff)
        lastVal = root.val
        dfs(root.right)

    dfs(root)
    return minDiff
