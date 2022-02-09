# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
def distanceK(root, target, K):
    ans = []
    visited = {}

    def findNodesDist(root):
        if not root:
            return -1

        if root is target:
            visited[root] = 0
            return 0

        left = dfs(root.left)
        if left != -1:
            visited[root] = left + 1
            return left + 1

        right = dfs(root.right)
        if right != -1:
            visited[root] = right + 1
            return right + 1

        return -1

    def dfs(root, depth, ans):
        if not root:
            return
        if root in visited:
            depth = visited[root]
        if depth == K:
            ans.append(root.val)

        dfs(root.left, depth+1, ans)
        dfs(root.right, depth+1, ans)

    findNodesDist(root)
    dfs(root, visited[root], ans)
    return ans
