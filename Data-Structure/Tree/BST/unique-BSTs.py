# https://leetcode.com/problems/unique-binary-search-trees-ii/
# https://leetcode.com/problems/unique-binary-search-trees/

def numTrees(n):
    G = [0] * (n+1)
    G[0], G[1] = 1, 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            G[i] += G[j-1] + G[i-j]

    return G[n]


def generateTrees(n):

    def buildTree(start, end):
        if start > end:
            return [None, ]
        allTrees = []

        for i in range(start, end+1):
            leftTrees = buildTree(start, i-1)
            rightTrees = buildTree(i+1, end)
            for l in leftTrees:
                for r in rightTrees:
                    curr = TreeNode(i)
                    curr.left = l
                    curr.right = r
                    allTrees.append(curr)
        return allTrees

    return buildTree(1, n) if n else []
