# https://leetcode.com/problems/binary-tree-maximum-path-sum/
#https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
def maxPathSum(root):
    maxsum = float("-inf")

    def dfs(root):
        if not root:
            return
        
        left_gain = max(dfs(root.left), 0)
        right_gain = max(dfs(root.right), 0)
        currsum = left_gain + root.val + right_gain
        maxsum = max(maxsum, currsum)
        return root.val + max(left_gain, right_gain)

    dfs(root)
    return maxsum