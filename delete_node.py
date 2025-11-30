def deleteNode(self, root, key):
        if not root:
            return None

        # search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # case 1 & 2: node with 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # case 3: node with 2 children
            # find inorder successor (smallest in right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left

            # replace value
            root.val = curr.val

            # delete inorder successor
            root.right = self.deleteNode(root.right, curr.val)

        return root
