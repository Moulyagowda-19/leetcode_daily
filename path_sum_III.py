def pathSum(self, root, targetSum):
        def dfs(node, currentSum):
            if not node:
                return 0

            currentSum += node.val

            count = prefixSum.get(currentSum - targetSum, 0)

            prefixSum[currentSum] = prefixSum.get(currentSum, 0) + 1

            count += dfs(node.left, currentSum)
            count += dfs(node.right, currentSum)

            prefixSum[currentSum] -= 1
            return count

        prefixSum = {0: 1} 
        return dfs(root, 0)