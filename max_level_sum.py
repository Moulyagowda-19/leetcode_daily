from collections import deque

class Solution:
    def maxLevelSum(self, root):
        if not root:
            return 0

        q = deque([root])
        level = 1
        max_sum = float('-inf')
        answer_level = 1

        while q:
            current_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                current_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if current_sum > max_sum:
                max_sum = current_sum
                answer_level = level

            level += 1

        return answer_level
