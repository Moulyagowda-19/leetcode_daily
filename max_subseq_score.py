import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        heap = []
        curr_sum = 0
        max_score = 0
        
        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            curr_sum += n1
            
            if len(heap) > k:
                curr_sum -= heapq.heappop(heap)
            
            if len(heap) == k:
                max_score = max(max_score, curr_sum * n2)
        
        return max_score
