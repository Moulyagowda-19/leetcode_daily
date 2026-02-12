class Solution:
    def singleNumber(self, nums):
        ans = 0
        for n in nums:
            ans ^= n
        return ans

        
