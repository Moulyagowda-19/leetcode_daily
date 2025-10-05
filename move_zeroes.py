def moveZeroes(self, nums):
       
        lastNonZeroIndex = 0  # position for next non-zero element

        # Step 1: Move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroIndex] = nums[i]
                lastNonZeroIndex += 1

        # Step 2: Fill remaining slots with zero
        for i in range(lastNonZeroIndex, len(nums)):
            nums[i] = 0
