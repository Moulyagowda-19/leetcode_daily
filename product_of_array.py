def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        # Step 1: Prefix product
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Step 2: Suffix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
        