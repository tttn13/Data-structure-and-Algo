def search(root, key):
    if not root:
        return
    if root.val == key:
        return root
    if key > root.val:
        return search(root.right)
    return search(root.left)
