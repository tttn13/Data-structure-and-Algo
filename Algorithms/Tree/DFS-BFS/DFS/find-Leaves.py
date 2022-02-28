# https://leetcode.com/problems/find-leaves-of-binary-tree/

from collections import defaultdict


def findLeaves(root):
    ans = defaultdict(list)

    def getDepth(root):  # post order traversal
        if not root:
            return 0

        leftDepth = getDepth(root.left)
        rightDepth = getDepth(root.right)

        depth = max(leftDepth, rightDepth) + 1
        ans[depth].append(root.val)
        return depth

    getDepth(root, 0)
    return ans.values()
