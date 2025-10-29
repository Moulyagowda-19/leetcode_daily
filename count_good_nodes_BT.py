def goodNodes(self, root):
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            # Check if the current node is good
            good = 1 if node.val >= max_so_far else 0
            
            # Update the max value for the path
            max_so_far = max(max_so_far, node.val)
            
            # Count good nodes in left and right subtrees
            good += dfs(node.left, max_so_far)
            good += dfs(node.right, max_so_far)
            
            return good
        
        return dfs(root, root.val)