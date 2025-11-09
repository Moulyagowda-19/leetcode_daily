def longestZigZag(self, root):
        self.ans = 0

        def dfs(node, direction, length):
            if not node:
                return
            
            # update global answer
            self.ans = max(self.ans, length)

            # if previous direction was left, go right
            if direction == "left":
                dfs(node.right, "right", length + 1)
                dfs(node.left, "left", 1)  # restart new zigzag
            else:
                dfs(node.left, "left", length + 1)
                dfs(node.right, "right", 1)  # restart new zigzag

        dfs(root, "left", 0)
        dfs(root, "right", 0)

        return self.ans