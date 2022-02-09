# https://leetcode.com/problems/minimum-absolute-difference-in-bst/


def getMinimumDifference(root):
    self.minDiff = self.lastVal = float("inf")
       # traverse inorderly to create a sorted arr

       def dfs(root):
            if not root:
                return

            dfs(root.left)
            self.minDiff = min(abs(root.val - self.lastVal), self.minDiff)
            self.lastVal = root.val
            dfs(root.right)

        dfs(root)
        return self.minDiff
