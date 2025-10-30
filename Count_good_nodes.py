def goodNodes(self, root):
        def dfs(node, max_val):
            if not node:
                return 0

            good = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)

            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)

            return good

        return dfs(root, root.val)
