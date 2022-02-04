# https://leetcode.com/problems/binary-tree-paths/

def binaryTreePaths(root):
    def traverse(root, isLeft, string):
        if root:
            string += "->" + str(root.val)
            if not root.left and not root.right:
                res.append(string)
                return
            traverse(root.left)
            traverse(root.right)

    res = []
    string = str(root.val)
    if not root.left and not root.right:
        return [string]
    else:
        traverse(root.left, True, string)
        traverse(root.right, False, string)
        return res
