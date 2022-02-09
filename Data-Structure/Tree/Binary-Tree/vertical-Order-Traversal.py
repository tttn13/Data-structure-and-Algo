# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
from collections import defaultdict
# O (W x H log H) : W is the width of the binary tree (i.e. the number of columns in the result) and HH is the height of the tree.


def verticalOrder(root):
    if not root:
        return []

    min_col = max_col = 0
    colTable = defaultdict(list)

    def dfs(root, row, col):
        if not root:
            return

        colTable[col].append((row, root.val))
        min_col = min(min_col, col)
        max_col = max(max_col, col)
        dfs(root.left, row+1, col-1)
        dfs(root.right, row+1, col+1)

    ans = []
    for col in range(min_col, max_col + 1):
        colTable[col].sort(key=lambda x: x[0])  # sort by row
        # extract the val from row,val tuple
        colVals = [val for row, val in colTable[col]]
        ans.append(colVals)
    return ans
