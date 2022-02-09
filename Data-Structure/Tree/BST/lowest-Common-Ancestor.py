# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

def LCA(root, p, q):
    if p.val < q.val:
        smaller, bigger = p, q
    else:
        smaller, bigger = q, p

    def traverse(root):
        if not root:
            return
        if smaller.val <= root.val <= bigger.val:
            return root
        if bigger.val < root.val:
            return traverse(root.left)
        if smaller.val > root.val:
            return traverse(root.right)

    return traverse(root)
