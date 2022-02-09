# https://leetcode.com/problems/binary-tree-right-side-view/

from collections import defaultdict


def rightSideView(root):
    table = defaultdict(list)

    def traverse(node, row, col):
        if not node:
            return
        table[row].append((col, node.val))
        traverse(node.left, row+1, col - 1)
        traverse(node.right, row+1, col+1)

    traverse(root, 0, 0)

    ans = []
    for r in table:
        ans.append(table[r][-1][1])
    return ans
