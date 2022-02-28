def findTilt(root):
    sum_of_tilt_nodes = 0

    def dfs(root):
        if not root:
            return 0
        left_sum = dfs(root.left)
        right_sum = dfs(root.right)
        sum_of_curr_nodes = left_sum + right_sum + root.val

        sum_of_tilt_nodes += abs(left_sum - right_sum)
        return sum_of_curr_nodes

    dfs(root)
    return sum_of_tilt_nodes
