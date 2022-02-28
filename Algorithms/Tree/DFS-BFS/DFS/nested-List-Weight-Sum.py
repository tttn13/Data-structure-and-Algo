# https://leetcode.com/problems/nested-list-weight-sum/

def nestedSum(nestList):

    def dfs(nestList, depth):
        total = 0
        for n in nestList:
            if n.isInteger():
                total += n.getInteger() * depth
            else:
                total += dfs(n.getList(), depth + 1)
        return total
    return dfs(nestList, 1)


def sumInverse(nestList):
    cals = []
    maxDepth = float("-inf")

    def dfs(nestList, d):
        maxDepth = max(maxDepth, d)
        for n in nestList:
            if n.isInteger():
                cals.append((n.getInteger(), d))
            else:
                dfs(n.getList(), d+1)
    total = 0
    for v, d in cals:
        total += v * (maxDepth - d + 1)
    return total
