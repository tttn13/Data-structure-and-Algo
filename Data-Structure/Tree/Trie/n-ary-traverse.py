# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
# https://leetcode.com/problems/n-ary-tree-preorder-traversal

def postorder(root):
    if not root:
        return []
    stack, output = [root, ], []
    while stack:
        node = stack.pop()
        output.append(node.val)
        for c in node.children:
            stack.append(c)
    return reversed(output)


def preorder(root):
    if not root:
        return []
    stack, output = [root, ], []
    while stack:
        node = stack.pop()
        output.append(node.val)
        for c in reversed(node.children):
            stack.append(c)
    return output


def recursive_preorder(root):
    if not root:
        return []
    ans = []
    ans.append(root.val)
    for c in root.children:
        ans.extend(recursive_preorder(c))
    return ans


def recursive_postorder(root):
    if not root:
        return []
    ans = []
    for c in root.children:
        ans.extend(recursive_postorder(c))

    ans.append(root.val)
    return ans
