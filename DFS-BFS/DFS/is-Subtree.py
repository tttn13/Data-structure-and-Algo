# https://leetcode.com/problems/subtree-of-another-tree/

def isSubtree(root, subTree):
    def isEqual(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return isEqual(root1.left, root2.left) and isEqual(root1.right, root2.right)

    def dfs(node):
        if not node:
            return False
        if root.val == subTree.val:
            if isEqual(root, subTree):
                return True
        return dfs(node.left) or dfs(node.right)

    return dfs(root)
