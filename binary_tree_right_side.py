def rightSideView(self, root):
        if not root:
            return []
        
        queue = [root]
        result = []
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.pop(0)
                
                # last node of the level = visible from right
                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result