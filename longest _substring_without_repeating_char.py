def lengthOfLongestSubstring(self, str):
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(str)):
            # If duplicate found, shrink window from left
            while str[right] in seen:
                seen.remove(str[left])
                left += 1
            
            # Add current character
            seen.add(str[right])
            
            # Update max length
            max_len = max(max_len, right - left + 1)

        return max_len

        