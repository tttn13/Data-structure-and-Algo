# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/solution/


def connect(root):

    def dfs(root):
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        dfs(root.left)
        dfs(root.right)
        return root


    def bfs(root):
        if not root:
            return
        leftmost = root
        while leftmost.left is not None:
            head = leftmost.left
            while head is not None:
                #connect children of same parent
                head.left.next = head.right
                #connect children of diff parent
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            leftmost = leftmost.left
        return root

    bfs(root)

    return root 