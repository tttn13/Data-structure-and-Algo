# https://leetcode.com/problems/increasing-order-search-tree/

def increasingBST(root):
    def dfs(node):
        if not node:
            return None
        dfs(node.left)
        node.left = None
        cur.right = node
        cur = node
        dfs(node.right)

    ans = cur = TreeNode(None)
    dfs(root)
    return ans.right
