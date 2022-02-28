# https://leetcode.com/problems/boundary-of-binary-tree/

def boundaryOfBinaryTree(root):
    boundary = [root.val]

    def dfs_leftmost(node):  # preorder
        if not node or (not node.left and not node.right):
            return
        boundary.append(node.val)
        if node.left:
            dfs_leftmost(node.left)
        else:
            dfs_leftmost(node.right)

    def dfs_leaves(node):  # inorder
        if not node:
            return
        dfs_leaves(node.left)
        if node is not root and (not node.left and not node.right):
            boundary.append(node.val)
        dfs_leaves(node.right)

    def dfs_rightmost(node):
        if not node or (not node.left and not node.right):
            return
        if node.right:
            dfs_rightmost(node.right)
        else:
            dfs_rightmost(node.left)
        boundary.append(node.val)

    if not root:
        return []
    dfs_leftmost(root.left)
    dfs_leaves(root)
    dfs_rightmost(root.right)
    return boundary