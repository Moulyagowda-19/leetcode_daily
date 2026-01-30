def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid  # ceil division

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left

        