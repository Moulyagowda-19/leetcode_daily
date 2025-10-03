def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)   # Find the current maximum candies any kid has
        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result
