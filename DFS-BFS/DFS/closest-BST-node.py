# https://leetcode.com/problems/closest-binary-search-tree-value/solution/
# 1. Recursive method, O(n)
def closestValue(root, target):
    def dfs(root):
        if root:
            minDiff = abs(root.val - target)
            if minDiff < res[1]:
                res = [root.val, minDiff]
            dfs(root.left)
            dfs(root.right)

    res = [root.val, 0]
    dfs(root)
    return res[0]


def closestValue(root, target):
    def binarySearch(root):
        closest = root.val
        while root:
            minDiff = min(root.val, closest, key=lambda x: abs(target - x)
            if root.val < target:
                root=root.left
            else:
                root=root.right
        return minDiff
    return binarySearch(root)
