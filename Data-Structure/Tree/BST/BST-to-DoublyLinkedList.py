# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
def treeToDLL(root):
    last = Node(None)
    first = Node(None)

    def dfs(root):
        if root:
            dfs(root.left)
            if last is None:
                first = root
            else:
                last.right = root
                root.left = last
            dfs(root.right)
    if not root:
        return None
    dfs(root)
    last.right = first
    first.left = last
    return first
