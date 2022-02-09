# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
def maxDepth(root):
    if not root:
        return 0
    stack = [(1, root), ]
    depth = 0
    while stack:
        currDepth, node = stack.pop()
        depth = max(depth, currDepth)
        for c in node.children:
            stack.append(((currDepth+1), c))
    return depth


def recursive_depth(root):
    self.maxDepth = 0

    def dfs(root, depth):
        if not root:
            return 0
        self.maxDepth = max(depth+1, self.maxDepth)
        for c in root.children:
            dfs(c, depth+1)

    dfs(root, 0)
    return self.maxDepth
