def maxDepth(self, root):
        if root is None:
            return 0
        leftd = self.maxDepth(root.left)
        rightd = self.maxDepth(root.right)
        return max(leftd,rightd)+1
        