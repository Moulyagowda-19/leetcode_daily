def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate area
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)
            
            # Move the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1     
        return max_area

