def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        
        # If root is one of the targets, return it
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q found in different subtrees → LCA found
        if left and right:
            return root
        
        # Otherwise return the non-null result
        return left if left else right
