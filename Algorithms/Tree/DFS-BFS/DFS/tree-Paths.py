# https://leetcode.com/problems/binary-tree-paths/

def binaryTreePaths(root):
    def traverse(root, string):
        if not root:
            return

        string += ("->" + str(root.val))
        if not root.left and not root.right:
            res.append(string[2:])
            return
        traverse(root.left, string)
        traverse(root.right, string)

    res = []
    string = str(root.val)
    if not root.left and not root.right:
        return [string]
    else:
        traverse(root, "")
        return res
