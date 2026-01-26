import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        left = []
        right = []
        
        i = 0
        j = len(costs) - 1
        
        # initialize heaps
        while i <= j and len(left) < candidates:
            heapq.heappush(left, costs[i])
            i += 1
        
        while i <= j and len(right) < candidates:
            heapq.heappush(right, costs[j])
            j -= 1
        
        total = 0
        
        for _ in range(k):
            if not right or (left and left[0] <= right[0]):
                total += heapq.heappop(left)
                if i <= j:
                    heapq.heappush(left, costs[i])
                    i += 1
            else:
                total += heapq.heappop(right)
                if i <= j:
                    heapq.heappush(right, costs[j])
                    j -= 1
        
        return total

        