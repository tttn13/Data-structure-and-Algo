# https://leetcode.com/problems/delete-nodes-and-return-forest/
# The question is composed of two requirements:

# To remove a node, the child need to notify its parent about the child's existance.
# To determine whether a node is a root node in the final forest, we need to know [1] whether the node is removed (which is trivial), and [2] whether its parent is removed (which requires the parent to notify the child)
# It is very obvious that a tree problem is likely to be solved by recursion. The two components above are actually examining interviewees' understanding to the two key points of recursion:

# passing info downwards -- by arguments
# passing info upwards -- by return value

def delNodes(root, to_delete):
    res = []
    to_delete = set(to_delete)

    def dfs(node, parent_not_exist):
        if not node: 
            return None
        if node.val in to_delete:
            node.left = dfs(node.left, True)
            node.right = dfs(node.right, True)
            return None
        else:
            if parent_not_exist:
                res.append(root)
            node.left = dfs(node.left, False)
            node.right = dfs(node.right, False)
            return node
    dfs(root, True)
    return res