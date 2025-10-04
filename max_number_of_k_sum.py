def maxOperations(self, nums, k):
        from collections import Counter
        
        count = Counter(nums)
        operations = 0
        
        for num in nums:
            if count[num] > 0 and count[k - num] > 0:
                if num == k - num and count[num] < 2:
                    continue
                count[num] -= 1
                count[k - num] -= 1
                operations += 1
                
        return operations
