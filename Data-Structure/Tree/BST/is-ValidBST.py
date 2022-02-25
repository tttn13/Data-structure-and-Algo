# https://leetcode.com/problems/validate-binary-search-tree/solution/

def isValidBST(root):
    last = -float("inf")

    def dfs(root):
        if not root:
            return True  # empty trees are valid BSTs

        left = dfs(root.left)
        if root.val <= self.last:
            return False
        self.last = root.val

        right = dfs(root.right)
        return left and right

    return dfs(root)
