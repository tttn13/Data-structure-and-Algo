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

def rightSideView_preorder(root):
    
    if not root: return []
    ans = []

    def dfs(root, depth): #reversed preorder - node - right - left
        if not root: return
        if len(ans) == depth:
            ans.append(root.val)
        dfs(root.right, depth+1)
        dfs(root.left, depth + 1)

    dfs(root, 0)
    return ans