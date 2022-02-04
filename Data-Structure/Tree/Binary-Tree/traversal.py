# Inorder, Preorder, Postorder traversal methods
def traversal(root):
    res = []

    def inorder(root):  # left node right
        if root:
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

    def preorder(root):  # node left right
        if root:
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

    def postorder(root):  # left right node
        if root:
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
